// $(document).ready(function () {
//     loadData();
// });

function loadData(id) {
    var $dynamic_table = $("#dynamic_table");
    $.ajax({
        type: 'GET',
        url: '/api/log/default/'+ id + '/',
        dataType: "json",
        success: function (data) {
            $dynamic_table.dynatable({
                dataset: {
                    records: data
                },
                features: {
                    pushState: false
                }

            });
        }
    });
}

$.dynatableSetup({
    table: {
        defaultColumnIdStyle: 'noStyle'
    }
});