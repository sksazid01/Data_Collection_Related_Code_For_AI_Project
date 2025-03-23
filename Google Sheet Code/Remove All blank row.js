
function removeBlankRowsInColumnB() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var numRows = data.length;

  for (var i = numRows - 1; i >= 0; i--) {
    if (data[i][1] === "") { // Check if column B (index 1) is empty
      sheet.deleteRow(i + 1); // Delete the row (i + 1 because rows are 1-indexed)
    }
  }
}
