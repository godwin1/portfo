from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


# @app.route('/')
# def home():
# 	return  render_template('./index.html')


@app.route('/<string:pages>')
def works(pages):
	return render_template(pages)

def dbase(data):
	with open('dbase.txt', mode ='a') as file:
		email = data['email']
		subject =data['subject']
		Message = data['msg']

		data = file.write(f'\n{email}, {subject}, {Message}');
		return data

def dbase_csv(data):
	with open('dbase.csv', mode ='a', newline ='') as csv_file:
		email = data['email']
		subject =data['subject']
		Message = data['msg']

		csv_writer = csv.writer(csv_file, delimiter =',', quotechar ='|', quoting=csv.QUOTE_MINIMAL);
		csv_writer.writerow([email, subject, Message])

@app.route('/submit_form', methods =['POST', 'GET'])
def submit_form():
	if request.method =='POST':
		try:
			data =request.form.to_dict()
			#dbase(data)
			dbase_csv(data)
			return redirect('/thank.html')
		except:
			return 'failed to save this data'
	else:
	  print('oops try again!')

# @app.route('/about.html')
# def about():
# 	return render_template('./about.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('./contact.html')

# @app.route('/components.html')
# def components():
# 	return render_template('./components.html')

# if __name__ == '__main__':
#    app.run(debug = True)