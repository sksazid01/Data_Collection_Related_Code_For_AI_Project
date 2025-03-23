function processAllChunkSheets() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  
  sheets.forEach(function(sheet) {
    var sheetName = sheet.getName();
    
    // Check if the sheet is a chunk sheet (e.g., named "ds1", "ds2", etc.)
    if (sheetName.startsWith('ds')) {
      Logger.log('Processing sheet: ' + sheetName);
      protectOddRows(sheet);
    }
  });
}

function protectOddRows(sheet) {
  var numRows = sheet.getMaxRows();
  var numCols = 4; // Only protect the first four columns

  for (var i = 1; i <= numRows; i += 2) { // Iterate over odd rows
    var rowData = sheet.getRange(i, 1, 1, numCols).getValues()[0];
    if (rowData.every(cell => cell === "")) {
      Logger.log('Empty row encountered at row ' + i + '. Stopping protection.');
      break; // Stop processing if an empty row is encountered
    }
    
    var range = sheet.getRange(i, 1, 1, numCols);
    var protection = range.protect().setDescription('Protect odd row ' + i);
    
    // Remove all editors except the owner
    protection.removeEditors(protection.getEditors());
    
    if (protection.canDomainEdit()) {
      protection.setDomainEdit(false);
    }
    
    // Allow only the specified email to edit
    protection.addEditor('example@gmail.com');
  }
}
