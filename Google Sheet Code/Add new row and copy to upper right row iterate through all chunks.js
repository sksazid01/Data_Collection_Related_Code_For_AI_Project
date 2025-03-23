function processAllChunkSheets() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  
  sheets.forEach(function(sheet) {
    var sheetName = sheet.getName();
    
    // Check if the sheet is a chunk sheet with a number 18 or greater
    if (sheetName.startsWith('ds')) {
      var sheetNumber = parseInt(sheetName.substring(2), 10); // Extract the number part
      if (sheetNumber >= 0) {
        Logger.log('Processing sheet: ' + sheetName);
        insertRowsWithFormulaAndColor(sheet);
      }
    }
  });
}

function insertRowsWithFormulaAndColor(sheet) {
  var data = sheet.getDataRange().getValues();
  var numRows = data.length;
  var numCols = data[0].length;

  for (var i = numRows - 1; i >= 0; i--) {
    if (data[i].some(cell => cell !== "")) {
      // Insert a new row below the current row
      sheet.insertRowAfter(i + 1);
      
      // Set the ">" value in the second column of the new row
      var newRowCell = sheet.getRange(i + 2, 2); // This targets column B of the new row
      newRowCell.setValue(">");

      // Set the background color to light green
      newRowCell.setBackground('#c1f7c1'); // Light green color

      // Add a formula to the cell in the row above, in the next column
      if (numCols > 1) { // Ensure there is more than one column
        var formulaCell = sheet.getRange(i + 1, 3); // This targets column C of the current row
        formulaCell.setFormula('=IF(LEFT(' + newRowCell.getA1Notation() + ', 1) = ">", MID(' + newRowCell.getA1Notation() + ', 2, LEN(' + newRowCell.getA1Notation() + ') - 1), ' + newRowCell.getA1Notation() + ')');
        
        // Set the background color of the formula cell to light green
        formulaCell.setBackground('#c1f7c1'); // Light green color
      }
    }
  }
}
