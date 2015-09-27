angular.module("callYourFolksApp")
.directive("contacts", function() {
    return {
        templateUrl: 'contacts/contacts.html',
    };
})
.factory("ContactsService", function($http) {
    var contactsServiceInstance;
    var contact_list = {
        contacts: [],
    };
    var load_contacts = function() {
        $http.get("/api/users/1")
        .then(function(data) {
            contact_list.contacts = data.data.contacts;
        }, function(data) {
            console.log("ERROR");
        });
    };

    contactsServiceInstance = {
        load_contacts: load_contacts,
        contact_list: contact_list,
    };

    return contactsServiceInstance;
})
.controller("ContactsController", function($scope, ContactsService) {
    $scope.contacts = [];

    $scope.$watch(function() {
        return ContactsService.contact_list.contacts;
    }, function(newValue, oldValue, scope) {
        console.log(newValue);
        if (newValue != oldValue) {
            $scope.contacts = newValue;
        }
    }, true);

});

