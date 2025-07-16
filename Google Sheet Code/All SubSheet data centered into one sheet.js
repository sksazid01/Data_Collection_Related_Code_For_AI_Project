// Create a new sheet named "Processed Data" with columns "Original" and "Local"
// Process each sheet from ds1 to ds13
// Place odd-numbered row content in column A (Original)
// Place even-numbered row content in column B (Local)


function processSheetsFast() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Create a new sheet for the processed data
  var newSheetName = "Processed Data";
  try {
    var existingSheet = ss.getSheetByName(newSheetName);
    if (existingSheet) {
      ss.deleteSheet(existingSheet);
    }
  } catch (e) {
    // Sheet doesn't exist, continue
  }
  
  var newSheet = ss.insertSheet(newSheetName);
  
  // Set up headers
  newSheet.getRange("A1").setValue("Original");
  newSheet.getRange("B1").setValue("Local");
  
  // Array to hold all processed data
  var processedData = [];
  
  // Process each sheet from ds1 to ds13
  for (var dsNum = 1; dsNum <= 13; dsNum++) {
    var sheetName = "ds" + dsNum;
    
    try {
      var currentSheet = ss.getSheetByName(sheetName);
      
      if (currentSheet) {
        var lastRow = currentSheet.getLastRow();
        if (lastRow > 0) {
          // Get all data at once
          var data = currentSheet.getRange("B1:B" + lastRow).getValues();
          
          // Process pairs of rows
          for (var i = 0; i < data.length; i += 2) {
            var original = data[i][0];
            var local = (i + 1 < data.length) ? data[i + 1][0] : "";
            
            if (original !== "" || local !== "") {
              processedData.push([original, local]);
            }
          }
        }
      }
    } catch (e) {
      Logger.log("Sheet " + sheetName + " not found or error: " + e.toString());
    }
  }
  
  // Write all data at once
  if (processedData.length > 0) {
    newSheet.getRange(2, 1, processedData.length, 2).setValues(processedData);
  }
  
  // Format the new sheet
  newSheet.autoResizeColumns(1, 2);
}
