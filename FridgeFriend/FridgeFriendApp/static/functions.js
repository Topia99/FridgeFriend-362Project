function addRow() {
    let table = document.getElementById("Items_Table");
    let row = table.insertRow(-1);
    let c1 = row.insertCell(0);
    let c2 = row.insertCell(1);
    let c3 = row.insertCell(2);
    items = document.getElementById("item").value
    expdate = document.getElementById("expdate").value
    c1.innerHTML = items
    c2.innerHTML = expdate
  }
  

function return_Date(item){
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();
  today = mm + '/' + dd + '/' + yyyy;
  time_left = today - item
  document.getElementById("date").innerHTML = time_left;
}