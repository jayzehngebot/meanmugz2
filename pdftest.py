import xhtml2pdf

def helloWorld():
	filename = __file__+".pdf"
	pdf = xhtml2pdf.document(
		"hello world",
		file(filename,"wb"))
	if not pdf.err:
		xhtml2pdf.startViewer(filename)

	if __name__ == "__main__":
		xhtml2pdf.showLogging()
		helloWorld()
