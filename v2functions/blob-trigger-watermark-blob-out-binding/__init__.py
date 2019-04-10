import logging
import azure.functions as func
import io
import sys
from PIL import Image

# Final image composite size
FINAL_COMPOSITE_MAX_HEIGHT = 700
FINAL_COMPOSITE_MAX_WIDTH = 700

# Set watermark 7 times smaller in width than base image
WATERMARK_WIDTH_RATIO = 7

# Note the type annotation for our output blob, func.Out[bytes],
# since it's an image we'll be writing back.
# See this for more -
# https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#outputs
# https://docs.microsoft.com/en-us/python/api/azure-functions/azure.functions.out?view=azure-python
def main(blobin: func.InputStream, blobout: func.Out[bytes], context: func.Context):
    logging.info(f"--- Python blob trigger function processed blob \n"
                 f"----- Name: {blobin.name}\n"
                 f"----- Blob Size: {blobin.length} bytes")
    
    # Pillow calls blobin.read() so only
    # pass in the image object
    input_image = blobin
    watermark_image = f'{context.function_directory}/watermark.png'

    try:
        base_image = Image.open(input_image)
        watermark = Image.open(watermark_image)
    except OSError as e:
        print(f'EXCEPTION: Unable to read input as image. {e}')
        sys.exit(254)
    except Exception as e:
        print(f'EXCEPTION: {e}')
        sys.exit(255)

    # Resize base image if too large
    if base_image.width > FINAL_COMPOSITE_MAX_WIDTH or base_image.height > FINAL_COMPOSITE_MAX_HEIGHT:
        if base_image.height > base_image.width:
            factor = 900 / base_image.height
        else:
            factor = 900 / base_image.width
        base_image = base_image.resize((int(base_image.width * factor), int(base_image.height * factor)))

    # Set watermark size
    relative_ws = round(base_image.width/WATERMARK_WIDTH_RATIO)
    watermark_size = (relative_ws, relative_ws)
    watermark.thumbnail(watermark_size, Image.ANTIALIAS)

    # Watermark anchor (left, top)
    position = (16, 16)
    
    img = Image.new('RGBA', (base_image.width, base_image.height), (0, 0, 0, 0))
    img.paste(base_image, (0, 0))
    # Watermark may not have an alpha channel,
    # therefore no mask to apply
    try:
        img.paste(watermark, position, mask=watermark)
    except ValueError:
        img.paste(watermark, position)
    # Render image on screen (save to a temp file and calls
    # xv on Linux and Preview.app on Mac)
    # We could improve this by drawing straight to a OpenCV
    # canvas.. maybe.
    img.show()

    # Store final composite in a memory stream
    img_byte_arr = io.BytesIO()
    # Convert composite to RGB so we can save as JPEG
    img.convert('RGB').save(img_byte_arr, format='JPEG')

    # Optionally, save final composite to disk
    # output_image = 'output.jpg'
    # img.save(output_image)

    # Write to output blob
    #
    # Use this to set blob content from a file instead:  
    # with open(output_image, mode='rb') as file:
    #     blobout.set(file.read())
    #
    # Set blob content from byte array in memory
    blobout.set(img_byte_arr.getvalue())

    logging.info(f"----- Watermarking successful")
