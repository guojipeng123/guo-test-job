(function () {
    $.atoms.cc_create_set = [
        {
            tag_code: "cc_set_parent_select",
            type: "tree",
            attrs: {
                name: gettext("父实例"),
                hookable: true,
                remote: true,
                remote_url: $.context.site_url + 'pipeline/cc_search_topo/set/prev/' + $.context.biz_cc_id + '/',
                remote_data_init: function (resp) {
                    return resp.data;
                },
                validation: [
                    {
                        type: "required"
                    }
                ]
            },
            methods: {}
        },
        {
            tag_code: "cc_set_info",
            type: "datatable",
            attrs: {
                name: gettext("集群信息"),
                remote_url: $.context.site_url + 'pipeline/cc_search_create_object_attribute/set/' + $.context.biz_cc_id + '/',
                remote_data_init: function(resp) {
                    return resp.data;
                },
                hookable: true,
                add_btn: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        }
    ]
})();
