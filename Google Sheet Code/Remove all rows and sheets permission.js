function removeAllProtections() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  
  sheets.forEach(function(sheet) {
    Logger.log('Removing protections from sheet: ' + sheet.getName());
    
    // Remove range protections
    var rangeProtections = sheet.getProtections(SpreadsheetApp.ProtectionType.RANGE);
    rangeProtections.forEach(function(protection) {
      protection.remove();
      Logger.log('Removed range protection from: ' + protection.getRange().getA1Notation());
    });
    
    // Remove sheet protections
    var sheetProtection = sheet.getProtections(SpreadsheetApp.ProtectionType.SHEET);
    sheetProtection.forEach(function(protection) {
      protection.remove();
      Logger.log('Removed sheet protection from: ' + sheet.getName());
    });
  });
}

// Main function to run the process
function main() {
  removeAllProtections(); // Remove all protections from all sheets
}
