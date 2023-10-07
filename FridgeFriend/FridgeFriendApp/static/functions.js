var rIndex, 
    table = document.getElementById("Items_Table")

function addRow() {
    
    var newRow = table.insertRow(table.length)
        c1 = newRow.insertCell(0)
        c2 = newRow.insertCell(1)
        c3 = newRow.insertCell(2)
        items = document.getElementById("item").value,
        expdate = document.getElementById("expdate").value,

    c1.innerHTML = items,
    c2.innerHTML = expdate,
    selectRowToInput();
  }
  
  function selectRow()
  {
    for(var i = 0; i < table.rows.length; i++)
    {
      table.rows[i].onclick = function()
      {
        rIndex = this.rowIndex
        document.getElementById("item").value = this.cells[0].innerHTML
        document.getElementById("expdate").value = this.cells[1].innerHTML
      }
    }
  }

  function delRow() 
  {
    table.rows[i].onclick = function()
    {
      rIndex = this.rowIndex
      table.deleteRow(rIndex)
    }
    
  }