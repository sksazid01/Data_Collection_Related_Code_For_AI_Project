function countWithGroupedOutput() {
  console.log("Starting count process...");
  console.log("Time: " + new Date());
  
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var totalCount = 0;
  var countGroups = {};
  
  // Collect data
  for (var i = 1; i <= 30; i++) {
    var sheetName = 'ds' + i;
    
    try {
      var sheet = ss.getSheetByName(sheetName);
      
      if (sheet) {
        var values = sheet.getRange('C1:C200').getValues();
        var sheetCount = 0;
        
        for (var j = 0; j < values.length; j++) {
          if (values[j][0] && values[j][0].toString().trim() !== '') {
            sheetCount++;
          }
        }
        
        totalCount += sheetCount;
        
        if (!countGroups[sheetCount]) {
          countGroups[sheetCount] = [];
        }
        countGroups[sheetCount].push(sheetName);
      }
    } catch (e) {
      console.error("Error with " + sheetName + ": " + e);
    }
  }
  
  // Display header
  console.log("\nCells    | Sheets");
  console.log("---------|-------------------------------------------------------");
  
  // Sort and display results
  var sortedCounts = Object.keys(countGroups).map(Number).sort(function(a, b) { return a - b; });
  
  sortedCounts.forEach(function(count) {
    var sheets = countGroups[count].join(', ');
    // Format count with left padding
    var countStr = count.toString();
    while (countStr.length < 8) {
      countStr = countStr + ' ';
    }
    console.log(countStr + " | " + sheets);
  });
  
  console.log("---------|-------------------------------------------------------");
  
  // Summary
  console.log("\nSummary:");
  var zeroSheets = countGroups[0] ? countGroups[0].length : 0;
  var hundredSheets = countGroups[100] ? countGroups[100].length : 0;
  var otherSheets = 30 - zeroSheets - hundredSheets;
  
  if (zeroSheets > 0) {
    console.log("• " + zeroSheets + " sheets with 0 cells");
  }
  if (hundredSheets > 0) {
    console.log("• " + hundredSheets + " sheets with 100 cells");
  }
  if (otherSheets > 0) {
    console.log("• " + otherSheets + " sheets with other counts");
  }
  console.log("• Total: " + totalCount + " cells across 30 sheets");
  
  console.log("\nProcess completed at: " + new Date());
  
  return totalCount;
}

// Even simpler version without any complex formatting
function countWithBasicGroupedOutput() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var totalCount = 0;
  var countGroups = {};
  
  // Collect data
  for (var i = 1; i <= 30; i++) {
    var sheetName = 'ds' + i;
    var sheet = ss.getSheetByName(sheetName);
    
    if (sheet) {
      var values = sheet.getRange('C1:C200').getValues();
      var count = 0;
      
      for (var j = 0; j < values.length; j++) {
        if (values[j][0] && values[j][0].toString().trim() !== '') {
          count++;
        }
      }
      
      totalCount += count;
      
      if (!countGroups[count]) {
        countGroups[count] = [];
      }
      countGroups[count].push(sheetName);
    }
  }
  
  // Display results
  console.log("\n=== COUNT SUMMARY ===");
  
  var counts = Object.keys(countGroups).map(Number).sort(function(a, b) { return a - b; });
  
  counts.forEach(function(count) {
    console.log(count + " cells: " + countGroups[count].join(', '));
  });
  
  console.log("\n=== STATISTICS ===");
  console.log("Total: " + totalCount + " cells");
  console.log("Sheets with 0 cells: " + (countGroups[0] ? countGroups[0].length : 0));
  console.log("Sheets with 100 cells: " + (countGroups[100] ? countGroups[100].length : 0));
  
  return totalCount;
}
