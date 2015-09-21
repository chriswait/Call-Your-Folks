angular.module("callYourFolksApp")
.directive("recommended", function() {
    return {
        templateUrl: 'recommended/recommended.html',
    };
})
.factory("RecommendedService", function($http, $q) {
    var recommendedServiceInstance;
    var recommended_calls = {
    };
    var load_recommended = function() {
        var url = "recommended";
        var request_params = {
            userId: 1,
        };
        var promise = $q(function(respond, reject) {
            $http({url:url, method:"GET", params:request_params})
            .then(function(data) {
                recommended_calls.recommended = data.data;
                respond(recommended_calls);
            }, function(data) {
                reject(data);
            });
        });
        return promise;
    };

    recommendedServiceInstance = {
        load_recommended: load_recommended,
        recommended_calls: recommended_calls,
    };
    return recommendedServiceInstance;
})
.controller("RecommendedController", function($scope, RecommendedService) {
    RecommendedService.load_recommended()
    .then(function(data) {
        console.log(data);
        $scope.recommended = RecommendedService.recommended_calls.recommended;
    });
});
