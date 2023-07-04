function setToMenuCart(menuItemId){
  setItemInCookie(menuItemId)

  document.getElementById("cart_item"+menuItemId).classList.toggle('hide');
  document.getElementById("cart_item"+menuItemId).classList.remove('show');
  document.getElementById("item"+menuItemId).classList.toggle('hide');

  document.getElementById("plus"+ menuItemId).classList.toggle('show');
  document.getElementById("plus_item"+menuItemId).classList.toggle('show_a');
  document.getElementById("plus"+ menuItemId).classList.remove('hide');

  document.getElementById("cart_quantity"+ menuItemId).innerHTML=1;

  document.getElementById("minus"+ menuItemId).classList.toggle('show');
  document.getElementById("minus_item"+menuItemId).classList.toggle('show_a');
  document.getElementById("minus"+ menuItemId).classList.remove('hide');

  document.getElementById("trash"+ menuItemId).classList.toggle('show');
  document.getElementById("trash"+ menuItemId).classList.remove('hide');
  document.getElementById("trash_bin"+menuItemId).classList.toggle('show_a');
}


function removeFromMenuCart(menuItemId){
  removeItemFromCookie(menuItemId)

  document.getElementById("cart_item"+menuItemId).classList.toggle('show');
  document.getElementById("cart_item"+menuItemId).classList.remove('hide');
  document.getElementById("item"+menuItemId).classList.toggle('show');
  document.getElementById("item"+menuItemId).classList.remove('hide');


  document.getElementById("plus"+ menuItemId).classList.toggle('hide'); 
  document.getElementById("plus_item"+menuItemId).classList.toggle('hide');
  document.getElementById("plus_item"+menuItemId).classList.remove('show_a');
  document.getElementById("plus"+ menuItemId).classList.remove('show');

  document.getElementById("cart_quantity"+ menuItemId).innerHTML="";


  document.getElementById("minus"+ menuItemId).classList.toggle('hide');
  document.getElementById("minus_item"+menuItemId).classList.toggle('hide');
  document.getElementById("minus_item"+menuItemId).classList.remove('show_a');
  document.getElementById("minus"+ menuItemId).classList.remove('show');

  document.getElementById("trash"+ menuItemId).classList.toggle('hide');
  document.getElementById("trash"+ menuItemId).classList.remove('show');
  document.getElementById("trash_bin"+menuItemId).classList.toggle('hide');
  document.getElementById("trash_bin"+menuItemId).classList.remove('show_a');
}

function decreaseFromMenuCart(menuItemId){
  let value = decreaseItemFromCookie(menuItemId)
  let quantity = value[menuItemId]['quantity']
  if (quantity<=0) {
    removeFromMenuCart(menuItemId)
    }
  else{
    document.getElementById("cart_quantity"+menuItemId).innerHTML=quantity;
  }
}

function removeFromCart(menuItemId,price) {
  let quantity = removeItemFromCookie(menuItemId)
  document.getElementById('cartItem'+menuItemId).innerHTML=""
  document.getElementById('cartItem'+menuItemId).classList.toggle('hide')
  let initial_total_price= document.getElementById('total_price').innerHTML
  document.getElementById('total_price').innerHTML=initial_total_price-(price*quantity)
}

function decreaseFromCart(menuItemId,price){
  let value = decreaseItemFromCookie(menuItemId)
  let quantity = value[menuItemId]['quantity']
  if (quantity<=0) {
    removeFromCart(menuItemId)
    }
  else{
    document.getElementById("cart_quantity"+ menuItemId).innerHTML=quantity;
    let initial_total_price= document.getElementById('total_price').innerHTML
    document.getElementById('total_price').innerHTML=initial_total_price-price
  }
}
function addToCart(menuItemId,price){
  addItemToCookie(menuItemId)
  let initial_total_price= document.getElementById('total_price').innerHTML
  console.log(initial_total_price+price)
  document.getElementById('total_price').innerHTML=(+initial_total_price + +price)
}

  function setItemInCookie(menuItemId) {
    let value=getCookie()
    value[menuItemId]={'quantity':1}
    document.cookie = 'cart' + "=" + JSON.stringify(value) + ";path=/";
  }


function addItemToCookie(menuItemId) {
    let value=getCookie()
    value[menuItemId]['quantity']+=1
    document.getElementById("cart_quantity"+ menuItemId).innerHTML=value[menuItemId]['quantity'];
    document.cookie = 'cart' + "=" + JSON.stringify(value) + ";path=/";
  }

function decreaseItemFromCookie(menuItemId) {
    let value=getCookie()
    value[menuItemId]['quantity']-=1
    document.cookie = 'cart' + "=" + JSON.stringify(value) + ";path=/";
    return value
  }

function removeItemFromCookie(menuItemId) {
    let value=getCookie()
    let quantity = value[menuItemId]['quantity']
    if (value[menuItemId]!=undefined)
    {
      delete value[menuItemId]
    }
    document.cookie = 'cart' + "=" + JSON.stringify(value) + ";path=/";
    return quantity
  }

function getCookie() {
    let name ="cart=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return JSON.parse(c.substring(name.length, c.length));
      }
    }
    return {};
  }
