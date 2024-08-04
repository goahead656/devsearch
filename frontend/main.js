// let loginBtn = document.getElementById('login-btn')
// let logoutBtn = document.getElementById('logout-btn')

// let token = localStorage.getItem('token')

// if(token){
//     loginBtn.remove()
// }else{
//     logoutBtn.remove()
// }

// logoutBtn.addEventListener('click',(e) =>{
//     e.preventDefault()
//     localStorage.removeItem('token')
//     window.location = 'file:///D:/code/python/django/devsearch/frontend/login.html'
// })


document.addEventListener('DOMContentLoaded', () => {
    let loginBtn = document.getElementById('login-btn');
    let logoutBtn = document.getElementById('logout-btn');

    let token = localStorage.getItem('token');

    if (token) {
        if (loginBtn) {
            loginBtn.remove();
        }
    } else {
        if (logoutBtn) {
            logoutBtn.remove();
        }
    }

    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.removeItem('token');
            window.location = 'file:///D:/code/python/django/devsearch/frontend/login.html';
        });
    }
});


let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects =()=>{
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data =>{
        console.log(data)
        buildProjects(data)
    })
}

let buildProjects = (projects) =>{
    let projectsWrapper = document.getElementById('projects-wrapper')

    for(let i=0;i<projects.length;i++){
        let project = projects[i]
        
        let projectCard = `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.featured_image}">

                    <div>
                        <div class="card--header">
                            <h3>${project.title}</h3>
                            <strong class="vote--option" data-vote='up' data-project="${project.id}">&#43;</strong>
                            <strong class="vote--option" data-vote='down' data-project="${project.id}">&#8722;</strong>
                        </div>
                        <i>${project.vote_ratio}</i>
                    </div>
                    <i>${project.title}% Positive feedback</i>
                    <p>${project.description.substring(0,150)}</p>
                </div>
        `
        projectsWrapper.innerHTML += projectCard
    }
    addVoteEvents()
}

let addVoteEvents = ()=>{
    let voteBtns = document.getElementsByClassName("vote--option")
    // console.log('VOTE BUTTONS:',voteBtns)
    for(let i=0;i<voteBtns.length;i++){
        voteBtns[i].addEventListener('click',(e) =>{
            // get token from frontend
            let token = localStorage.getItem('token')

            // let token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyODQ1ODQ3LCJpYXQiOjE3MjI3NTk0NDcsImp0aSI6IjE3Yzg4OGYxYzcxYTRkYTBiNjFlMDg2ZGI4OWFmMjk2IiwidXNlcl9pZCI6NH0.TBx_1Lcz5oyd_S5mL3TvGXfng90_OVvxUFMxn4H451M'
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project

            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`,{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    Authorization: `Bearer ${token}`
                },
                body:JSON.stringify({'value':vote})
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:',data)
                })
        })
    }
}

getProjects()
