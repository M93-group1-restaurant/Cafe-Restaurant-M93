function show_allorders(){
    document.getElementById("recent").hidden=true;
    document.getElementById("pending").hidden=true;
    document.getElementById("confirmed").hidden=true;
    document.getElementById("cooking").hidden=true;
    document.getElementById("canceled").hidden=true;
    document.getElementById("all_orders").hidden=false;
}

function show_pending(){
    document.getElementById("recent").hidden=true;
    document.getElementById("pending").hidden=false;
    document.getElementById("confirmed").hidden=true;
    document.getElementById("cooking").hidden=true;
    document.getElementById("canceled").hidden=true;
    document.getElementById("all_orders").hidden=true;
}

function show_cooking(){
    document.getElementById("recent").hidden=true;
    document.getElementById("pending").hidden=true;
    document.getElementById("confirmed").hidden=true;
    document.getElementById("cooking").hidden=false;
    document.getElementById("canceled").hidden=true;
    document.getElementById("all_orders").hidden=true;
}

function show_paid(){
    document.getElementById("recent").hidden=true;
    document.getElementById("pending").hidden=true;
    document.getElementById("confirmed").hidden=false;
    document.getElementById("cooking").hidden=true;
    document.getElementById("canceled").hidden=true;
    document.getElementById("all_orders").hidden=true;
}

function show_canceled(){
    document.getElementById("recent").hidden=true;
    document.getElementById("pending").hidden=true;
    document.getElementById("confirmed").hidden=true;
    document.getElementById("cooking").hidden=true;
    document.getElementById("canceled").hidden=false;
    document.getElementById("all_orders").hidden=true;
}

function show_recent(){
    document.getElementById("recent").hidden=false;
    document.getElementById("pending").hidden=true;
    document.getElementById("confirmed").hidden=true;
    document.getElementById("cooking").hidden=true;
    document.getElementById("canceled").hidden=true;
    document.getElementById("all_orders").hidden=true;
}