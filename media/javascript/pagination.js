var mockup, 
    parent_mockup,
    isLoading = false
    hasMore = true;

var per_page,page;

var target = $(window);

$(document).ready(function(){
    noHasMoreElement = $("#noHasMore");
    loadingElement = $("#loading");
    mockup = $(".mockupItem");
    if(mockup){
        parent_mockup = mockup.parent();

        per_page = 10;
        page = 1;

        showItems();

        target.scroll(function(event){
            loadItems();
        });
    }
});

function showNoHasMore(){
    parent_mockup.append(noHasMoreElement);
    noHasMoreElement.fadeIn('slow').delay(2000).fadeOut('slow');
}

function addLoading(){
    parent_mockup.append(loadingElement);
    loadingElement.fadeIn('slow');
}

function removeLoading(){
    loadingElement.hide();
}

function loadItems(){
    var mayLoadContent = target.scrollTop() + 10 >= $(document).height() - target.height();
    if (mayLoadContent) {
        //setTimeout('showItems()', 0);
        showItems();
    }
}

function clearItems(){
    parent_mockup.empty();
}

function filterItems(){
    // TODO change url
    clearItems()
    showItems();
}

function showItems(){
    if (!hasMore){
        showNoHasMore();
        return;
    }
    if(!isLoading){
        isLoading = true;
        addLoading();

        var pagination_details = "&per_page="+per_page+"&page="+page;
        
        var separe_filters = /\?[\w\W]*/g;
        var filters =  window.location.href.match(separe_filters);
        if (filters) {
            filters = filters[0].replace(/\?/, '') + pagination_details;
        } else {
            filters = pagination_details.replace(/&/, '');
        }
        
        var base_url = window.location.href.replace(separe_filters,'');
        var has_back_slash = /\/$/;
        base_url = has_back_slash.test(base_url) ? base_url : base_url + "/";
        base_url = base_url + "buscar";

        $.getJSON(base_url, filters).done(function(items){
            //TODO improve this, change to a callback
            removeLoading();

            //User eval to parse an string to array?
            //Only array ?
            if(items.length < 1){
                hasMore = false;
                showNoHasMore();
                return;
            }

            $.each(items, function(index, item){
                addDynamicItem(item, ".mockupItem");
            });

            isLoading = false;
        });

        page++;
    }
}

function addDynamicItem(json, itemSelector){
    var item = $(itemSelector);
    var parent = item.parent();
    var htmlItem = item.html();
    htmlItem = decodeURI(htmlItem);

    var html_wildcard_pattern = /{\s*[\.\w]*\s*}/g;

    try{
        var values = htmlItem.match(html_wildcard_pattern);
        $.each(values, function(index, value){
            var exp_call = value.replace(/[{}\s]/g,'');

            var last_word_after_dot_pattern = /\w*$/;
            exp_call = exp_call.replace(json.model.match(last_word_after_dot_pattern),'json');

            var id_pattern = /\.id/;
            if(id_pattern.test(exp_call)){
                exp_call = exp_call.replace(id_pattern,'.pk');
            } else {
                var field_name = exp_call.match(last_word_after_dot_pattern);
                exp_call = exp_call.replace(field_name,'fields.'+field_name);
            }

            htmlItem = htmlItem.replace(value, eval(exp_call));

        });
        parent.append(item.clone().html(htmlItem).removeClass('mockupItem').addClass('item'));
    }catch(error){
        console.log('error to show - ' + json + ' ' + error.message);
    }
}