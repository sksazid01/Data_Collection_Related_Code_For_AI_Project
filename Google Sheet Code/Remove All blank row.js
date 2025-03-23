function removeBlankRowsInColumnB() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var numRows = data.length;
  var rowsToDelete = [];

  // Collect indices of rows to delete
  for (var i = 0; i < numRows; i++) {
    if (data[i][1] === "" || data[i][1] === " " ) { // Check if column B (index 1) is empty
      rowsToDelete.push(i + 1); // Store the 1-indexed row number
    }
  }

  // Delete rows in reverse order to avoid shifting issues
  for (var j = rowsToDelete.length - 1; j >= 0; j--) {
    sheet.deleteRow(rowsToDelete[j]);
  }
}
