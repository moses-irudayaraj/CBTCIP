from flask import Flask, redirect, url_for, render_template, request, abort

app = Flask(__name__)

import random
player = 0
opponent = 0
time = 1
pl_ts=0
opp_ts=0
@app.route('/')
def index():
    global player
    global opponent
    player = random.randint(1,10)
    isTrue=True
    pl_ts=0
    opp_ts=0
    if(player%2==0):
        opponent=1
        player = 2
    else:
        opponent=2
        player=1
    if time==2:
        player=2
    if player==1:
        return redirect(url_for('player'))
    else:
        return redirect(url_for('opponent'))


@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/opponent')
def opponent():
    return render_template('opponent.html')

# pl_num = int(input(f"\n\nPlayer{player} please enter a Multi-Digit Number: "))
# pl_num = str(pl_num)
pl_num = ''
@app.route('/process', methods=['POST'])
def process():
    global player
    global opponent
    if (request.method == 'POST'):
        global pl_num
        pl_num = str(request.form['mult_digit'])
    if player==2:
        return redirect(url_for('play1_space'))
    else:
        return redirect(url_for('play2_space'))

result=''
EndRes=''
@app.route('/play1_space')
def play1_space():
    global result
    global pl_num
    global EndRes
    return render_template('play2_space.html',result=result,num=len(pl_num),EndRes=EndRes)

@app.route('/play2_space')
def play2_space():
    global result
    global pl_num
    global EndRes
    return render_template('play1_space.html',result=result,num=len(pl_num),EndRes=EndRes)
        
      
@app.route('/p1logic', methods=['POST'])
def p1logic():
    global time
    global pl_ts
    global result
    global pl_num
    global EndRes

    

    if 'guess' in request.form:
        opp_num = request.form['guess']
        g_p = 0
        pl_ts += 1
        result = ''

        for i in range(len(pl_num)):
            if pl_num[i] == opp_num[i]:
                result += opp_num[i]
                g_p += 1
            else:
                result += '_'

        if g_p == len(pl_num):
            EndRes = 'Excellent you guessed right!'
            EndRes += " The number of times you tried: " + str(pl_ts)
            if pl_ts == 1:
                Final = "\n <br> Congrats Mastermind! player1 you won in the first attempt itself!!!"
                return render_template('FinalResult.html', Final=Final)
            if time==1:
                time=2
                return render_template('player.html')
            else:
                return redirect(url_for('gameend'))

    return render_template('play1_space.html', result=result, num=len(pl_num), EndRes=EndRes)


@app.route('/p2logic', methods=['POST'])
def p2logic():
    global result
    global opp_ts
    global time
    global EndRes
    global pl_num

   
    if 'guess' in request.form:
        opp_num = request.form['guess']
        g_o = 0
        opp_ts += 1
        result = ''

        for i in range(len(pl_num)):
            if pl_num[i] == opp_num[i]:
                result += opp_num[i]
                g_o += 1
            else:
                result += '_'

        if g_o == len(pl_num):
            EndRes = 'Excellent you guessed right!'
            EndRes += " The number of times you tried: " + str(opp_ts)
            if opp_ts == 1:
                final = "\n Congrats Mastermind! player2 you won in the first attempt itself!!!"
                return render_template('FinalResult.html', Final=final)
            if time==1:
                time=2
                return render_template('opponent.html')
            else:
                return redirect(url_for('gameend'))

    return render_template('play1_space.html', result=result, num=len(pl_num), EndRes=EndRes)
@app.route('/gameend')
def gameend():
    if(opp_ts<pl_ts):
        final = " Congrats player"+str(opponent)+" you won"
    else:
        final = " Congrats player"+str(player)+" you won"
    return render_template('FinalResult.html',final = final)

if __name__ == '__main__':
    app.run(debug=True)
