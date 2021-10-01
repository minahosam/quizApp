// console.log('hi')
const modalButtons=[...document.getElementsByClassName('quiz-modal')]
// console.log(modalButtons)
const info=document.getElementById('modal-info')
const start = document.getElementById('start-quiz')
const url = window.location.href
modalButtons.forEach(modalButton=>modalButton.addEventListener('click',()=>{
    // console.log(modalButton)
    const pk=modalButton.getAttribute('data-pk')
    // console.log(pk)
    const name=modalButton.getAttribute('data-name')
    const difficulty=modalButton.getAttribute('data-difficulty')
    const question=modalButton.getAttribute('data-numberofquestion')
    const time=modalButton.getAttribute('data-time')
    const score=modalButton.getAttribute('data-score')
    info.innerHTML=`
        <div class='mb-3 h5'>Are You Sure You Want To Start Quiz <b>${name}</b> ?</div>
        <div class='muted'>
            <ul>
                <li>number of questions:${question}</li>
                <li>difficulty:${difficulty}</li>
                <li>quiz time:${time} min</li>
                <li>score to pass :${score} %</li>
            </ul>
        </div>
    `
    start.addEventListener('click',()=>{
        window.location.href=url+pk
    })
})) 