from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
app =  Flask(__name__)




@app.route('/')
def otherStuff():


	author = "Arsalaan"
	name = "Ansari"
	return render_template('index.html', author =author, name = name)

@app.route('/analytics', methods=['GET','POST'])
def analytics():
	if request.method == 'POST':
		return render_template('analytics.html')
	else:
		return 'not post'

if __name__ == '__main__':
	app.run(debug = True)

urlparse.uses_netloc.append("postgres")

url = urlparse.urlparse(os.environ["DATABASE_URL"])
print (url)

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)



