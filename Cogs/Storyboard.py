from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import os, sys, json
FilePath = os.path.dirname(os.path.abspath(__file__))

def LoadStory(to_load):
    if sys.platform == "linux" or sys.platform == "linux2":
        with open(f"{FilePath}/Files/Storys/{to_load}.json", "r") as JSON:
            return json.load(JSON)
    if sys.platform == "win32" or sys.platform == "win64":
        with open(f"{FilePath}\\Files\\Storys\\{to_load}.json", "r") as JSON:
            return json.load(JSON)

def LoadTemplates():
    if sys.platform == "linux" or sys.platform == "linux2":
        with open(f"{FilePath}/Files/SBTemplates.json", "r") as JSON:
            return json.load(JSON)
    if sys.platform == "win32" or sys.platform == "win64":
        with open(f"{FilePath}\\Files\\SBTemplates.json", "r") as JSON:
            return json.load(JSON)

def GetTemplate(Template):
    RawTemplates = LoadTemplates()

    ImageSize = RawTemplates[Template]["ImageSize"]
    BackGroundSize = RawTemplates[Template]["BackGroundSize"]
    BackGroundLocation = RawTemplates[Template]["BackGroundLocation"]
    TextSize = RawTemplates[Template]["TextSize"]
    TextLocation = RawTemplates[Template]["TextLocation"]
    FaceSize = RawTemplates[Template]["FaceSize"]
    FaceLocation = RawTemplates[Template]["FaceLocation"]
    BorderSize = RawTemplates[Template]["BorderSize"]
    BorderLocation = RawTemplates[Template]["BorderLocation"]
    TextBorderSize = RawTemplates[Template]["TextBorderSize"]
    TextBorderLocation = RawTemplates[Template]["TextBorderLocation"]
    FaceBorderSize = RawTemplates[Template]["FaceBorderSize"]
    FaceBorderLocation = RawTemplates[Template]["FaceBorderLocation"]

    return ImageSize,BackGroundSize,BackGroundLocation,TextSize,TextLocation,FaceSize,FaceLocation,BorderSize,\
           BorderLocation,TextBorderSize, TextBorderLocation, FaceBorderSize, FaceBorderLocation


def MakeSB(Template,BackGround,Face,Text,Border,TextBorder,FaceBorder):

    ImageSize, BackGroundSize, BackGroundLocation, TextSize, TextLocation, FaceSize, FaceLocation, BorderSize,\
    BorderLocation, TextBorderSize, TextBorderLocation, FaceBorderSize, FaceBorderLocation = GetTemplate(Template)

    SBImage = Image.new("RGBA", ImageSize, (0, 0, 0, 0))

    if BackGround != None:
        if len(BackGround) != 0:
            if sys.platform == "linux" or sys.platform == "linux2":
                with Image.open(f"{FilePath}/Files/Images/BackGround/{BackGround}.png") as BackGroundImage:
                    BackGroundImage.thumbnail(BackGroundSize)
                    SBImage.paste(im=BackGroundImage, box=BackGroundLocation)
            if sys.platform == "win32" or sys.platform == "win64":
                with Image.open(f"{FilePath}\\Files\\Images\\BackGround\\{BackGround}.png") as BackGroundImage:
                    BackGroundImage.thumbnail(BackGroundSize)
                    SBImage.paste(im=BackGroundImage, box=BackGroundLocation)

    if Face != None:
        if len(Face) != 0:
            if sys.platform == "linux" or sys.platform == "linux2":
                with Image.open(f"{FilePath}/Files/Images/Face/{Face}.png") as FaceImage:
                    FaceImage.thumbnail(FaceSize)
                    SBImage.paste(im=FaceImage, box=FaceLocation, mask=FaceImage)
            if sys.platform == "win32" or sys.platform == "win64":
                with Image.open(f"{FilePath}\\Files\\Images\\Face\\{Face}.png") as FaceImage:
                    FaceImage.thumbnail(FaceSize)
                    SBImage.paste(im=FaceImage, box=FaceLocation, mask=FaceImage)

    if Border != None:
        if len(Border) != 0:
            if sys.platform == "linux" or sys.platform == "linux2":
                with Image.open(f"{FilePath}/Files/Images/Border/{Border}.png") as BorderImage:
                    BorderImage.thumbnail(BorderSize)
                    SBImage.paste(im=BorderImage, box=BorderLocation, mask=BorderImage)
            if sys.platform == "win32" or sys.platform == "win64":
                with Image.open(f"{FilePath}\\Files\\Images\\Border\\{Border}.png") as BorderImage:
                    BorderImage.thumbnail(BorderSize)
                    SBImage.paste(im=BorderImage, box=BorderLocation, mask=BorderImage)

    if TextBorder != None:
        if len(TextBorder) != 0:
            if sys.platform == "linux" or sys.platform == "linux2":
                with Image.open(f"{FilePath}/Files/Images/TextBorder/{TextBorder}.png") as TextBorderImage:
                    TextBorderImage.thumbnail(TextBorderSize)
                    SBImage.paste(im=TextBorderImage, box=TextBorderLocation, mask=TextBorderImage)
            if sys.platform == "win32" or sys.platform == "win64":
                with Image.open(f"{FilePath}\\Files\\Images\\TextBorder\\{TextBorder}.png") as TextBorderImage:
                    TextBorderImage.thumbnail(TextBorderSize)
                    SBImage.paste(im=TextBorderImage, box=TextBorderLocation, mask=TextBorderImage)

    if FaceBorder != None:
        if len(FaceBorder) != 0:
            if sys.platform == "linux" or sys.platform == "linux2":
                with Image.open(f"{FilePath}/Files/Images/FaceBorder/{FaceBorder}.png") as FaceBorderImage:
                    FaceBorderImage.thumbnail(FaceBorderSize)
                    SBImage.paste(im=FaceBorderImage, box=FaceBorderLocation, mask=FaceBorderImage)
            if sys.platform == "win32" or sys.platform == "win64":
                with Image.open(f"{FilePath}\\Files\\Images\\FaceBorder\\{FaceBorder}.png") as FaceBorderImage:
                    FaceBorderImage.thumbnail(FaceBorderSize)
                    SBImage.paste(im=FaceBorderImage, box=FaceBorderLocation, mask=FaceBorderImage)

    if Text != None:
        if len(Text) != 0:
            Font = ImageFont.truetype('C:\\Windows\\Fonts\\LINBIOLINUM_R_G.ttf', TextSize[0])


            BlurryText = Image.new('RGBA', ImageSize)
            NewTextLocation = TextLocation[1]
            for line in textwrap.wrap(Text, width=TextSize[1]):
                BlurryTextDraw = ImageDraw.Draw(BlurryText)
                BlurryTextDraw.multiline_text((TextLocation[0]+.5, NewTextLocation+.7), line, font=Font, fill="#fff")
                NewTextLocation += Font.getsize(line)[1]
            BlurryText = BlurryText.filter(ImageFilter.GaussianBlur(1))
            SBImage.paste(im=BlurryText, box=[0,0], mask=BlurryText)
            NewTextLocation = TextLocation[1] = TextLocation[1]


            for line in textwrap.wrap(Text, width=TextSize[1]):
                TextDraw = ImageDraw.Draw(SBImage)
                TextDraw.multiline_text((TextLocation[0], NewTextLocation), line, font=Font, fill="#000")
                NewTextLocation += Font.getsize(line)[1]
    return SBImage

def GetSBInfo(Scenario,Part="10",GetFullStory=False):
    FullStory = LoadStory("StoryDB")
    if GetFullStory == True:
        return FullStory
    Template = FullStory[Scenario][Part]['Template']
    BackGround = FullStory[Scenario][Part]['BackGround']
    Face = FullStory[Scenario][Part]['Face']
    Text = FullStory[Scenario][Part]['Text']
    Choices = {"Scenario": Scenario}
    Border = FullStory[Scenario][Part]['Border']
    TextBorder = FullStory[Scenario][Part]['TextBorder']
    FaceBorder = FullStory[Scenario][Part]['FaceBorder']
    for each in FullStory[Scenario][Part]['Choices']:
        Choices.update({each: FullStory[Scenario][Part]['Choices'][each]})
    return Template, BackGround, Face, Text, Choices, Border, TextBorder, FaceBorder

def SBImageAssembly(Scenario, Part):
    Template, BackGround, Face, Text, Choices, Border, TextBorder, FaceBorder = GetSBInfo(Scenario, Part)
    SBImage = MakeSB(Template, BackGround, Face, Text, Border, TextBorder, FaceBorder)
    if sys.platform == "linux" or sys.platform == "linux2":
        SBImage.save(f"{FilePath}/Files/Images/TEMP.png")
    if sys.platform == "win32" or sys.platform == "win64":
        SBImage.save(f"{FilePath}\\Files\\Images\\TEMP.png")
    return Choices
