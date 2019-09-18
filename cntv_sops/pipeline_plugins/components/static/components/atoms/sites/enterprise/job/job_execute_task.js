(function () {
    $.atoms.job_execute_task = [
        {
            tag_code: "job_task_id",
            type: "select",
            attrs: {
                name: gettext("作业模板"),
                hookable: false,
                remote: true,
                remote_url: $.context.site_url + 'pipeline/job_get_job_tasks_by_biz/' + $.context.biz_cc_id + '/',
                remote_data_init: function (resp) {
                    return resp.data;
                },
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "job_global_var",
            type: "datatable",
            attrs: {
                name: gettext("全局变量"),
                hookable: true,
                empty_text: gettext("没选中作业模板或当前作业模板全局变量为空"),
                columns: [
                    {
                        tag_code: "id",
                        type: "text",
                        attrs: {
                            name: "ID",
                            hidden: true
                        }
                    },
                    {
                        tag_code: "name",
                        type: "text",
                        attrs: {
                            name: gettext("参数名称"),
                        }
                    },
                    {
                        tag_code: "type",
                        type: "text",
                        attrs: {
                            name: gettext("参数类型"),
                            hidden: true,
                        }
                    },
                    {
                        tag_code: "value",
                        type: "textarea",
                        attrs: {
                            name: gettext("参数值"),
                            editable: true
                        }
                    },
                    {
                        tag_code: "description",
                        type: "text",
                        attrs: {
                            name: gettext("描述")
                        }
                    }
                ]
            },
            events: [
                {
                    source: "job_task_id",
                    type: "change",
                    action: function (value) {
                        var $this = this;
                        this.set_loading(true);
                        $.ajax({
                            url: $.context.site_url + 'pipeline/job_get_job_detail_by_biz/' + $.context.biz_cc_id + '/' + value + '/',
                            type: 'GET',
                            dataType: 'json',
                            success: function (resp) {
                                $this._set_value(resp.data.global_var);
                                $this.set_loading(false);
                            },
                            error: function () {
                                $this._set_value([]);
                                $this.set_loading(false);
                            }
                        });
                    }
                }
            ]
        }
    ]
})();