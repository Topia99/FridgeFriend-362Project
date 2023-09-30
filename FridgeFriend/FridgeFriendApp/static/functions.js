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
  

  function deleteRow(r) 
  {
    let table = document.getElementById("Items_Table");

  
  }