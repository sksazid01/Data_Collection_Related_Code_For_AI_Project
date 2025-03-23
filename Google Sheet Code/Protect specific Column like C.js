function protectColumnC() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  
  sheets.forEach(function(sheet) {
    var sheetName = sheet.getName();
    Logger.log('Protecting column C in sheet: ' + sheetName);
    
    // Define the range to protect (column C)
    var range = sheet.getRange('C:C');
    
    // Protect the range
    var protection = range.protect().setDescription('Protect column C');
    
    // Remove all editors except the owner
    protection.removeEditors(protection.getEditors());
    
    if (protection.canDomainEdit()) {
      protection.setDomainEdit(false);
    }
    
    // Optionally, add specific users who can edit
    protection.addEditor('ahasanulhaque20@gmail.com');
  });
}
