from flask import Flask, render_template, request, redirect, url_for
from forms import LibraryForm
from models import library
UPLOAD_FOLDER='uploads'

app = Flask(__name__)
app.config["SECRET_KEY"]="jsfjsfejlopkn"


@app.route("/library/", methods=['GET','POST'])
def library_view():
   form=LibraryForm()
   error=""
   if request.method=='POST':
      if form.validate_on_submit():
         library.create(form.data)
         library.save_all()
      return redirect(url_for("library_view"))
   return render_template("library.html", form=form, library=library.all(), error=error)


@app.route("/library/<int:library_id>/", methods=['GET', 'POST'])
def position_details(library_id):
   position = library.get(library_id -1)
   form = LibraryForm(data=position)
   if request.method=='POST':
      if form.validate_on_submit():
         library.update(library_id -1, form.data)
      return redirect(url_for("library_view"))
   return render_template("library_id.html", form=form, library_id=library_id)


if __name__ == "__main__":
    app.run(debug=True)



