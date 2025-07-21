function removeGreaterThanFromColumnB() {
  // Get the active sheet
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Processed Data");
  
  if (!sheet) {
    SpreadsheetApp.getUi().alert('Sheet "Processed Data" not found!');
    return;
  }
  
  // Get all data from column B (column 2)
  var lastRow = sheet.getLastRow();
  var range = sheet.getRange(1, 2, lastRow, 1); // Column B is column 2
  var values = range.getValues();
  
  var modifiedCount = 0;
  
  // Process each cell
  for (var i = 0; i < values.length; i++) {
    if (values[i][0]) {
      var cellText = String(values[i][0]);
      if (cellText.charAt(0) === '>') {
        values[i][0] = cellText.substring(1);
        modifiedCount++;
      }
    }
  }
  
  // Write back to sheet
  range.setValues(values);
  
  SpreadsheetApp.getUi().alert('Completed! Modified ' + modifiedCount + ' cells in column B.');
}
