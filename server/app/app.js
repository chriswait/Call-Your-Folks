var app = angular.module("callYourFolksApp", ['templates', 'ngMaterial', 'ngMdIcons']);
app.controller("MainController", function(ContactsService) {
    ContactsService.load_contacts();
});
