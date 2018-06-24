
angular.module('myApp', [])
.controller('myCtrl', ['$scope', function($scope) {
    $scope.today = new Date();
    $scope.name = "";
    $scope.values_1 = [];
    $scope.value1 = 0;
    $scope.value2 = 0;
    $scope.count = 0;
    $scope.selectedType = "";
    $scope.name = "";
    $scope.myFunc = function() {
        $scope.count++;
        alert("INFO: ");
    };
    $scope.types = ["Neurologista", "Cardiologista", "Oftalmologista", "Dermatologista"];
    $scope.mySub = function() {
        alert("Requerimento enviado!");
    };

}])
