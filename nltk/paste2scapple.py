import nltk
import os
import pyperclip

appearance = """\
			<Appearance>
				<Alignment>Left</Alignment>
				<Border Weight="0" Style="Rounded"/>
			</Appearance>"""

others = """\
	<BackgroundShapes/>
	<NoteStyles>
		<Style Name="Big 12" ID="D842EDB8-17B1-4E6C-A74A-8671F0E8AFB2" AffectFontStyle="Yes" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<FontSize>12.0</FontSize>
		</Style>
		<Style Name="Big 14" ID="2EAD375A-53B1-4807-A06E-845803EDAED7" AffectFontStyle="Yes" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<FontSize>14.0</FontSize>
		</Style>
		<Style Name="Big 17" ID="FFA0D3E3-C505-46C0-ACA0-D05C736BA185" AffectFontStyle="Yes" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<FontSize>17.0</FontSize>
		</Style>
		<Style Name="Big 20" ID="A54EAAA6-9491-4E7E-9873-9702886B55B8" AffectFontStyle="Yes" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<FontSize>20.0</FontSize>
		</Style>
		<Style Name="Big 24" ID="B6803718-C9F1-42C0-8588-A4D60C8E25C5" AffectFontStyle="Yes" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<FontSize>24.0</FontSize>
		</Style>
		<Style Name="Bubble Blue" ID="D5A51309-FBFD-4FC1-AC9C-74A087073622" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectSize="No" AffectFade="No" AffectSticky="No">
			<BorderThickness>1</BorderThickness>
			<BorderColor>0.561855 0.71062 0.779401</BorderColor>
			<FillColor>0.702319 0.888276 0.974252</FillColor>
		</Style>
		<Style Name="Bubble Green" ID="022EE2C1-7800-4238-8030-FDA5AED74BA0" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectSize="No" AffectFade="No" AffectSticky="No">
			<BorderThickness>1</BorderThickness>
			<BorderColor>0.572684 0.758969 0.558154</BorderColor>
			<FillColor>0.715855 0.948712 0.697692</FillColor>
		</Style>
		<Style Name="Bubble Pink" ID="CCD5C5EB-A5BD-41BE-8E4D-EA79221CEE82" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectSize="No" AffectFade="No" AffectSticky="No">
			<BorderThickness>1</BorderThickness>
			<BorderColor>0.794796 0.560965 0.58607</BorderColor>
			<FillColor>0.957566 0.766747 0.999616</FillColor>
		</Style>
		<Style Name="Bubble Red" ID="2BA7D3F8-D0A0-46C3-B3D2-9F5E81A25E03" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectSize="No" AffectFade="No" AffectSticky="No">
			<BorderThickness>1</BorderThickness>
			<BorderColor>0.794796 0.560965 0.58607</BorderColor>
			<FillColor>0.993495 0.701207 0.732587</FillColor>
		</Style>
		<Style Name="Bubble Yellow" ID="490B258A-EEB2-43DB-BC2E-0A0002C37BF1" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectSize="No" AffectFade="No" AffectSticky="No">
			<BorderThickness>1</BorderThickness>
			<BorderColor>0.798177 0.714184 0.522055</BorderColor>
			<FillColor>0.997722 0.89273 0.652569</FillColor>
		</Style>
		<Style Name="Red Text" ID="A739060C-79D1-416C-B537-A18F2BFCF957" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="Yes" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<TextColor>0.985948 0.0 0.026951</TextColor>
		</Style>
		<Style Name="Size 500" ID="F1835B32-89C3-43D2-84DA-0BA0D27767DF" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="No" AffectSize="Yes" AffectFade="No" AffectSticky="No">
			<Size>500.0,-1.0</Size>
		</Style>
		<Style Name="Title Text" ID="3083800F-E6D5-4946-9419-3C10F712687E" AffectFontStyle="Yes" AffectAlignment="Yes" AffectTextColor="No" AffectNoteBody="No" AffectSize="No" AffectFade="No" AffectSticky="No">
			<FontSize>24.0</FontSize>
			<IsBold>Yes</IsBold>
		</Style>
	</NoteStyles>
	<UISettings>
		<BackgroundColor>0.999767 0.98837 0.949907</BackgroundColor>
		<DefaultFont>Helvetica</DefaultFont>
		<DefaultTextColor>0.0 0.0 0.0</DefaultTextColor>
	</UISettings>
	<PrintSettings VerticalPagination="Auto" HorizontalPagination="Clip" Orientation="Portrait" RightMargin="12.000000" BottomMargin="12.000000" HorizontallyCentered="Yes" ScaleFactor="1.000000" PagesAcross="1" PaperType="na-letter" PagesDown="1" TopMargin="12.000000" Collates="Yes" PaperSize="-1.000000,-1.000000" LeftMargin="12.000000" VerticallyCentered="Yes"/>"""

def tokenizer(text):
	processed = ""
	sentences = nltk.tokenize.sent_tokenize(text)
	for sentence in sentences:
		lines = sentence.splitlines()
		for line in lines:
			if line.strip() != "":
				processed += f"{line}\n"
	return processed

def scapple(processed):
	path = os.path.join(os.environ['USERPROFILE'], "Desktop", "Processed.scap")
	with open(path, "w", encoding="utf-8") as file:
		file.write(f"""<?xml version='1.0' encoding='UTF-8' standalone='no'?>\n""")
		file.write(f"""<ScappleDocument ID="00000000-0000-0000-0000-000000000000" Version="1.1">\n""")
		file.write(f"""\t<Notes>\n""")

		x = 25.0
		y = 25.0
		width = 500.0
		for i, line in enumerate(processed.splitlines()):
			file.write(f"""\t\t<Note Width="{width}" FontSize="12" ID="{i}" Position="{x},{y}">\n""")
			file.write(f"""{appearance}\n""")
			file.write(f"""\t\t\t<String>{line}</String>\n""")
			file.write(f"""\t\t</Note>\n""")
			if i == 0:
				y += 35
			else:
				y += 60

		file.write(f"""\t</Notes>\n""")
		file.write(f"""{others}\n""")
		file.write(f"""</ScappleDocument>\n""")

text = pyperclip.paste()
processed = tokenizer(text)
scapple(processed)