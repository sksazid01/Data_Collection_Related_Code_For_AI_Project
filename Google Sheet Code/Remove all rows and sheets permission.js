function removeAllProtections() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  
  sheets.forEach(function(sheet) {
    Logger.log('Removing protections from sheet: ' + sheet.getName());
    
    // Get all protections on the sheet
    var protections = sheet.getProtections(SpreadsheetApp.ProtectionType.RANGE);
    
    // Remove each protection
    protections.forEach(function(protection) {
      protection.remove();
      Logger.log('Removed protection from range: ' + protection.getRange().getA1Notation());
    });
  });
}
