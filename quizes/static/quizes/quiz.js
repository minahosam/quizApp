// console.log('m')
const url = window.location.href
// console.log(url)
var quizBox=document.getElementById('quiz-box')
const resultBox = document.getElementById('result-box')
const scoreBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer')
const activateTimer=(time)=>{
    // console.log(time)
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }
    let minute= time - 1
    let second= 60
    let displayMinute
    let displaySecond
    const timer=setInterval(()=>{
        second --
        if (second < 0) {
            second =59
            minute --
        }
        if (minute.toString().length < 2) {
            displayMinute = '0' + minute
        }else{
            displayMinute = minute
        }
        if (second.toString().length < 2) {
            displaySecond= '0' + second
        } else {
            displaySecond = second
        }
        if (minute === 0 && second === 0) {
            timerBox.innerHTML=`<b>00:00</b>`
            setTimeout(() => {
                // alert('timeout')
                clearInterval(timer)
                alert('Time over')
                sendQuestion()
            }, 500)
        }
        timerBox.innerHTML=` <b>${displayMinute}:${displaySecond}</b>`
    },1000)
}
$.ajax({
    type:'GET',
	url:`${url}data`,
    success:function(response){
        // console.log(response)
        const data=response.data
        // console.log(data)
        data.forEach(e=>{
            for (const [q,a] of Object.entries(e)){
                // console.log(q)
                // console.log(a)
                quizBox.innerHTML += `
                    <hr>
                    <div class='mb-3'>
                        <b>${q}</b>
                    </div>
                    <hr>
                `
                a.forEach(answer=>{
                    quizBox.innerHTML+=` 
                    <div>
                        <input type='radio' class='an' id='${q}--${answer}' name='${q}' value='${answer}'>
                        <label for=${q}>${answer}</label>
                    </div>
                    `
                })
            };
        });
        activateTimer(response.time)
    },
    error:function(error){
        console.log(error)
    }
})
const quizForm=document.getElementById('quizForm')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const sendQuestion=()=>{
const answers = [...document.getElementsByClassName('an')]
    const data={}
    data['csrfmiddlewaretoken']=csrf[0].value
    answers.forEach(answer=>{
        if (answer.checked){
            data[answer.name]=answer.value
        } else {
            if (!data[answer.name]){
                data[answer.name]=null
            }
        }
        })
    $.ajax({
        type:'POST',
        url:`${url}save/`,
        data:data,
        success:function(response){
            // console.log(response)
            const quizResult=response.result
            // console.log(quizResult)
            scoreBox.innerHTML += `${response.passed ? 'congrats':'ups.'},${response.score.toFixed(2)}%`
            quizForm.classList.add('hidden')
            quizResult.forEach(res=>{
                // console.log(res)
                const resdiv=document.createElement('div')
                for (const[question,correct_answer] of Object.entries(res)){
                    // console.log(question)
                    // console.log(correct_answer)
                        // console.log(correct)
                        // console.log(ans)
                    resdiv.innerHTML += question
                    const cls = ['container','p-3','text-light','h5']
                    resdiv.classList.add(...cls)
                    if (correct_answer['answer'] == 'no-answer'){
                        const correct =correct_answer['correct']
                        resdiv.innerHTML += 'not answered'
                        resdiv.innerHTML += `correct:${correct}`
                        resdiv.classList.add('bg-danger')
                    }
                    else {
                        const qu_answer = correct_answer['answer']
                        const correct =correct_answer['correct']
                        if (qu_answer == correct) {
                            resdiv.classList.add('bg-success')
                            resdiv.innerHTML += `answer:${qu_answer}`
                        }
                        else {
                            resdiv.classList.add('bg-danger')
                            resdiv.innerHTML +- `answer: ${qu_answer} | correct: ${correct}`
                        }
                    }
                }
                // const body =document.getElementsByTagName('BODY')[0]
                // body.append(resdiv)
                resultBox.append(resdiv)
            })
        },
        error:function(error){
            console.log(error)
        }
    })
}
quizForm.addEventListener('submit',e=>{
    e.preventDefault();
    sendQuestion()
})