import asyncio
import io
import os.path

from PIL import Image
import aiohttp_jinja2
from aiohttp import web

from app.pictures.db_connection import path_redactor, get_img_name, get_img, put_img


@aiohttp_jinja2.template('show.html')
class ShowHandler(web.View):
    async def get(self):
        form = self.request.match_info.get('id', 0)
        path = get_img(int(form))
        return {"path": path}


@aiohttp_jinja2.template('upload.html')
class UploadHandlerGet(web.View):
    async def get(self):
        print('get')
        return


@aiohttp_jinja2.template('upload.html')
class UploadHandlerPost(web.View):

    async def post(self):
        post = await self.request.post()
        image = post.get("image")
        if image:
            img_content = image.file.read()
            buf = io.BytesIO(img_content)
            img = Image.open(buf)
            if int(post.get("y")) != 0:
                width = int(post.get("y"))
            else:
                width = img.width

            if int(post.get("x")) != 0:
                height = int(post.get("x"))
            else:
                height = img.height
            print(width, height)
            img = img.resize((width, height))
            curr = 0
            filename = 'app/pictures/img/%s.jpeg' % image.filename
            fn = image.filename
            while os.path.exists(filename):
                curr = curr + 1
                print(curr)
                filename = 'app/pictures/img/%s.jpeg' % (image.filename + str(curr))
            if curr != 0:
                fn = fn + str(curr)
            print(filename)
            img.save(filename)
            put_img(fn)
        return
