pm.test("Checking for Address", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.resolvedAddress).to.eql("Hyderabad, TS, India");
    });

pm.test("Checking for timezone", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.timezone).to.eql("Asia/Kolkata");
    });

    pm.test("Check Latitude", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.latitude).to.eql(17.3949);
    });

pm.test("Check Longitude", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.longitude).to.eql(78.4708);
    });

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});