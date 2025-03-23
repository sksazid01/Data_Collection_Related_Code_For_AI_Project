function processAllChunkSheets() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  
  sheets.forEach(function(sheet) {
    var sheetName = sheet.getName();
    
    // Check if the sheet is a chunk sheet starting from "ds3"
    if (sheetName.startsWith('ds')) {
      var sheetNumber = parseInt(sheetName.substring(2), 10); // Extract the number part
      if (sheetNumber >= 1) { // Start processing from "ds3"
        Logger.log('Processing sheet: ' + sheetName);
        protectOddRows(sheet);
      }
    }
  });
}

function protectOddRows(sheet) {
  var numRows = sheet.getMaxRows();
  var numCols = 4; // Only protect the first four columns
  var rangesToProtect = [];

  for (var i = 1; i <= numRows; i += 2) { // Iterate over odd rows
    var rowData = sheet.getRange(i, 1, 1, numCols).getValues()[0];
    if (rowData.every(cell => cell === "")) {
      Logger.log('Empty row encountered at row ' + i + '. Stopping protection.');
      break; // Stop processing if an empty row is encountered
    }
    
    rangesToProtect.push(sheet.getRange(i, 1, 1, numCols));
  }
  
  if (rangesToProtect.length > 0) {
    var protection = sheet.protect().setDescription('Protect odd rows');
    protection.setUnprotectedRanges(rangesToProtect);
    
    // Remove all editors except the owner
    protection.removeEditors(protection.getEditors());
    
    if (protection.canDomainEdit()) {
      protection.setDomainEdit(false);
    }
    
    // Allow only the specified email to edit
    protection.addEditor('ahasanulhaque20@gmail.com');
  }
}
