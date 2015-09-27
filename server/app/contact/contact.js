angular.module("callYourFolksApp")
.directive("contact", function() {
    return {
        templateUrl: 'contact/contact.html'
    };
})
.controller("ContactController", function($scope, $filter, $http, ContactsService) {
    var get_call_on_date = function(date) {
        for (var i = 0; i < $scope.contact.calls.length; i++) {
            call = $scope.contact.calls[i];
            if (call.date == date) return call;
        }
        return undefined;
    };

    $scope.days = [];
    var number_of_days_back = 10;
    var number_of_days_forward = 10;
    var ms_per_day = 24*60*60*1000;

    var today = new Date(); // Current moment
    var startDate = new Date(today.getTime() - number_of_days_back * ms_per_day);
    var endDate = new Date(today.getTime() + number_of_days_forward * ms_per_day);

    var formatted, did_call;
    var day_index = 0 - number_of_days_back;
    while (startDate <= endDate) {
        formatted = $filter('date')(startDate,"yyyy-MM-dd");
        call = get_call_on_date(formatted);
        day = {
            date: formatted,
            day_index: day_index,
            call: call,
        };
        day_index++;
        $scope.days.push(day);
        startDate.setDate(startDate.getDate() + 1); // Switch to next day
    }
    $scope.toggle_call = function(day) {
        var url;
        var contactId = $scope.contact.id;
        var userId = 1;
        var date = day.date;
        var request_params = {
            date: date,
            contactId: contactId,
            userId: userId,
        };
        if ((typeof day.call != "undefined") && (day.call.happened))
            url = 'delete_call';
        else
            url = 'log_call';
        $http({url:url, method:"GET",params:request_params})
        .then(function(data) {
            console.log(data);
            ContactsService.load_contacts();
        }, function(data) {
            console.log(data);
        });
    };
});
