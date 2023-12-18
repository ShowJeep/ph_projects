


const btns = document.querySelectorAll(".menu");
btns[0].style.backgroundColor = '#FD0606';

btns.forEach(btn => {
    btn.addEventListener('click', () => {
        btns.forEach(otherBtn => {
            otherBtn.style.backgroundColor = '';
        });
        btn.style.backgroundColor = '#FD0606';
    });
});


const loadData = (id) => {
    if(id==1){
        id=1000;
        fetch(` https://openapi.programming-hero.com/api/videos/category/${id}`)
        .then((res) => res.json())
        .then((val) => display(val.data.sort));
    }
    else{
        fetch(` https://openapi.programming-hero.com/api/videos/category/${id}`)
        .then((res) => res.json())
        .then((val) => display(val.data));
    }
    
};

const display = (val) => {
    const vdo = document.getElementById("videos");
    vdo.innerHTML = '';

    if(val.length==0){
        const card= document.createElement("div");
            card.classList.add("box");
            card.innerHTML=`
            <img class="box-img" src="./resource/Icon.png" alt=""></img>
            <h2>Oops!! Sorry, There is no 
            content here</h2>
            `;
            vdo.appendChild(card);
    }
    else{
        val.forEach((data) => {
            console.log(data);
            const card= document.createElement("div");
            card.classList.add("box");
            const verifiedLogo = data.authors[0].verified ? '<img class="verified-logo" src="./resource/blue_tick.png" alt="Verified">' : '';

                const time = data.others.posted_date ? convert(parseInt(data.others.posted_date)) : '';
                

            card.innerHTML=`
            <div class="thumb">
                <img class="box-img" src=${data.thumbnail} alt="">
                ${time ? `<p class="img-txt">${time.days} days ${time.hours} hours ${time.minutes} minutes ago</p>` : '<p class="img-txt"></p>'}
            </div>
            
            <div class="inner">
                <img class="pp-img" src=${data.authors[0].profile_picture} alt="">
                <h2>${data.title}</h2>
            </div>
            <p>${data.authors[0].profile_name}  ${verifiedLogo}</p>
            <p>${data.others.views} views</p>
            `;
            vdo.appendChild(card);
        });
    }
};

function convert(x){
    const days = Math.floor(x / (24 * 3600));
    const hours = Math.floor((x % (24 * 3600)) / 3600);
    const minutes = Math.floor((x % 3600) / 60);

    return {
        days: days,
        hours: hours,
        minutes: minutes
    };
}

loadData(1000);


document.getElementById('newtab').addEventListener('click', function(){
    const newTab = window.open('', '_blank');
    newTab.document.write(`
    <h1>Discuss the scope of var, let, and const:</h1>
    <h3>var is function scope, let and const is block scope. Variables declared with var can be used as global variable, while let and const are limited to their block and can not be used outside of the block.</h3>
    <br><br><br>
    <h1>Tell us the use cases of null and undefined:</h1>
    <h3>undefined indicates the automatic absence of a value, such as when a variable is declared but not assigned. On the other hand null is explicitly used to represent the intentional absence of any object value.</h3>
    <br><br><br>
    <h1>What do you mean by REST API?</h1>
    <h3>REST API, or Representational State Transfer Application Programming Interface, is an architectural style for designing networked applications using a stateless, client-server model and standard HTTP methods. 
    It emphasizes the use of resources and standard communication protocols for interactions between clients and servers.</h3>
    `);
    newTab.document.close();
});