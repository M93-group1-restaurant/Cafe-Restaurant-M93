function setCookie(menuItemId, quantity) {
    console.log(menuItemId)
    console.log(quantity)
    const value=getCookie()
    console.log(value)
    value[menuItemId]={'quantity':quantity}
    console.log(value)
    document.cookie = 'cart' + "=" + JSON.stringify(value) + ";path=/";
    console.log(document.cookie)
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
        console.log(c.substring(name.length, c.length))
        return JSON.parse(c.substring(name.length, c.length));
      }
    }
    return {};
  }
