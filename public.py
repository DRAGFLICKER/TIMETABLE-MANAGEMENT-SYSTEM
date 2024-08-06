from flask import *
from database import *
import csv
import os
import librosa
import numpy as np

public = Blueprint('public', __name__)

# @public.route('/')
# def training():
#     header = 'chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
#     for i in range(1, 21):
#         header += ' mfcc' + str(i)
#     header += ' label'
#     header = header.split()

#     with open('data.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(header)

#     genres = ['1', '2']

#     c = []

#     for g in genres:
#         folder_path = "static\\trainaudio\1" + g
#         for filename in os.listdir(folder_path):
#             songname = os.path.join(folder_path, filename)
#             print(songname, "jjjjj")

#             try:
#                 y, sr = librosa.load(songname, mono=True)
#                 chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
#                 spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
#                 spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
#                 rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
#                 zcr = librosa.feature.zero_crossing_rate(y)
#                 mfcc = librosa.feature.mfcc(y=y, sr=sr)

#                 to_append = str(np.mean(chroma_stft)) + " " + str(np.mean(spec_cent)) + " " + str(np.mean(spec_bw)) + " " + str(np.mean(rolloff)) + " " + str(np.mean(zcr))

#                 aa = [np.mean(chroma_stft), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]

#                 for e in mfcc:
#                     to_append += " " + str(np.mean(e))
#                     aa.append(np.mean(e))

#                 to_append += " " + g
#                 aa.append(g)

#                 with open('data.csv', 'a', newline='') as file:
#                     writer = csv.writer(file)
#                     writer.writerow(to_append.split())

#                 c.append(aa)
#             except Exception as e:
#                 print(f"Error processing {songname}: {e}")

#     return render_template('a.html', c=c)


@public.route('/')
def home():
	return render_template('publichome.html')

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if "login" in request.form:
		u=request.form['uname']
		p=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		print(q)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=="admin":
				flash("Logging in")			
				return redirect(url_for("admin.adminhome"))


 
			elif res[0]['user_type']=="user":
				q="select * from user where login_id='%s'"%(res[0]['login_id'])
				res1=select(q)
				if res1:
					session['uid']=res1[0]['user_id']
					print(session['uid'])
					flash("Logging in")
					return redirect(url_for("user.userhome"))

			else:
				flash("LOGIN Under Process")
		flash("Incorrect password")

	return render_template('login.html')
