
//zoom sui prezzi
var prezzi = document.querySelectorAll(".prezzi");

prezzi.forEach(function(element){

    element.addEventListener("mouseover",function(){
        this.style.fontSize = "24px";
    });

    element.addEventListener("mouseout",function(){
        this.style.fontSize = "20px";
    });

});


//zoom card con effetto ombra
let carta = document.querySelectorAll(".carta");

carta.forEach(function(carta){
    carta.addEventListener("mouseover",function(){
        this.classList.add('effetto-ombra')
    });

    carta.addEventListener("mouseout",function(){
        this.classList.remove('effetto-ombra')
    });

});


//bottone scheda allenamento
document.getElementById("bottone_scheda").addEventListener("click",function(){
    let scheda = document.getElementById("scheda_allenamento");
    if(scheda.style.display === "none"){
        scheda.style.display = "block";
    }
    else{
        scheda.style.display = "none";
    }
});

//dark mode

function dark_mode(){
    //prendo il tag <html> e i tag <tema>
    const htmlElement = document.querySelector('html');
    const temaObj = document.querySelectorAll('.tema');

    //se in dark mode già
    if (htmlElement.getAttribute('data-bs-theme')==='dark'){
        //tolgo dal <html> data-bs-theme
        htmlElement.removeAttribute('data-bs-theme');
        //metto le classi per il testo chiaro e tolgo quelle per lo scuro
        temaObj.forEach(function(elemento) {
            elemento.classList.remove('bg-dark', 'text-white');
            elemento.classList.add('bg-light', 'text-dark');
        });
    }
    //se in light mode
    else{
        //metto dentro <html> data-bs-theme
        htmlElement.setAttribute('data-bs-theme','dark');
        //per ogni classe tema tolgo le classi chiare e metto le classi scure
        temaObj.forEach(function(el){
            el.classList.remove('bg-light','text-dark');
            el.classList.add('bg-dark', 'text-white');
        })
    }
}

/*dark mode on loading page
window.onload = function() {
    // Qui metti la tua funzione da chiamare
    dark_mode();
    console.log("pagina caricata");
};*/




