import os

from PIL import Image

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Cm, Pt

from django.conf import settings


class PitchDeckGenerator:
    def __init__(self, slides_content,
                 template_name, logo_path,
                 presentation_path) -> None:
        self.slides_content = slides_content
        self.logo_path = logo_path
        self.presentation_path = presentation_path
        self.template = os.path.join(settings.BASE_DIR,
                                     'presentations',
                                     'pres_templates',
                                     f'{template_name}.pptx')

    def delete_first_slides(self, presentation, first_num):
        slide_ids = reversed(range(first_num))
        for slide_id in slide_ids:
            if slide_id < len(presentation.slides):
                xml_slides = presentation.slides._sldIdLst
                slides = list(xml_slides)
                xml_slides.remove(slides[slide_id])

    def create_ppt(self):

        prs = Presentation(self.template)

        title_slide_layout = prs.slide_layouts[0]
        content_slide_layout = prs.slide_layouts[1]

        # # add title slide
        # slide = prs.slides.add_slide(title_slide_layout)
        # title = slide.shapes.title
        # title.text = presentation_title

        # #add subtitle
        # subtitle = slide.placeholders[1]
        # subtitle.text = f"Presented by {presenter_name}"

        # if template_choice == 'dark_modern':
        #     for paragraph in title.text_frame.paragraphs:
        #         for run in paragraph.runs:
        #             run.font.name = 'Times New Roman'
        #             run.font.color.rgb = RGBColor(255, 165, 0)  # RGB for orange color

        # add content slides
        for slide_content in self.slides_content:
            slide = prs.slides.add_slide(content_slide_layout)
            for placeholder in slide.placeholders:
                if placeholder.placeholder_format.type == 1:  # Title
                    placeholder.text = slide_content['title']
                    for paragraph in placeholder.text_frame.paragraphs:
                        for run in paragraph.runs:
                            run.font.name = 'Arial'
                            # run.font.color.rgb = RGBColor(255, 165, 0)
                            run.font.size = Pt(25)
                elif placeholder.placeholder_format.type == 4:  # Content
                    placeholder.text = slide_content['content']
                    for paragraph in placeholder.text_frame.paragraphs:
                        for run in paragraph.runs:
                            run.font.name = 'Arial'
                            # run.font.color.rgb = RGBColor(255, 255, 255)
                            run.font.size = Pt(11)

            if self.logo_path:
                # add the image at the specified position
                slide_width = Cm(16)
                slide_height = Cm(9)

                im = Image.open(self.logo_path)
                width, height = im.size

                image_width, image_height = Cm(width / 700), Cm(height / 700)

                left = slide_width - image_width + Cm(8)   # calculate left position
                top = slide_height - image_height - Cm(5)  # calculate top position

                slide.shapes.add_picture(self.logo_path,
                                         left, top,
                                         width=image_width,
                                         height=image_height)

        # Delete the first twelve slides after all new slides have been added
        self.delete_first_slides(prs, 12)

        # Save the presentation
        prs.save(self.presentation_path)
        return prs
