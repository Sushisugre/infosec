ANDREWID = jsmith
DATE = 0904
PAPER = AssignmentTemplate
LATEX = latex
PDFLATEX = pdflatex
#TEXFILES = *.tex figures/*.tex
TEXFILES = *.tex
# BIBFILE = 
# EPSFILES = fig/*.eps

default: $(PAPER).pdf
	cp $(PAPER).pdf $(ANDREWID)-$(DATE).pdf

eps:	$(EPSFILES)

$(PAPER).dvi: $(TEXFILES) $(EPSFILES) $(BIBFILE) makefile
	$(LATEX) $(PAPER)
#	bibtex $(PAPER)
	$(LATEX) $(PAPER)
	$(LATEX) $(PAPER)

$(PAPER).pdf: $(TEXFILES) $(EPSFILES) $(ELFFILES) $(BIBFILE) makefile
	$(PDFLATEX) $(PAPER)
#	bibtex $(PAPER)
#	$(PDFLATEX) $(PAPER)
	$(PDFLATEX) $(PAPER)

## $(PAPER).pdf: $(PAPER).ps
## 	ps2pdf $(PAPER).ps

.PHONY: epspdf
epspdf: $(EPSFILES) $(PDFFILES)
	for i in $(EPSFILES); do \
	  epstopdf $$i; \
	done

# $(PAPER).pdf: $(PAPER).dvi
# 	dvipdf $(PAPER).dvi $(PAPER).pdf

$(PAPER).ps: $(PAPER).dvi
	dvips -P cmz -t letter -o $(PAPER).ps $(PAPER).dvi

final:	$(PAPER).pdf $(PAPER).ps
	cp $(PAPER).pdf final.pdf
	cp $(PAPER).ps final.ps

dvi: $(PAPER).dvi

ps: $(PAPER).ps

pdf: $(PAPER).pdf

preview: $(PAPER).dvi
	xdvi $(PAPER).dvi &

prevps: $(PAPER).ps
	ghostview $(PAPER).ps &

sendps: $(PAPER).ps
	sz $(PAPER).ps

sendpdf: $(PAPER).pdf
	sz $(PAPER).pdf

print: $(PAPER).ps
	lpr -Pmax $(PAPER).ps

clean:
	rm -f *.ps *.dvi *.aux *.bbl *.blg *.log $(PAPER).pdf $(ANDREWID)-$(DATE).pdf *~

wc:
	wc -w $(TEXFILES)

ispell:
	ispell -b -t $(TEXFILES)
