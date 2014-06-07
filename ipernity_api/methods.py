__methods__ = {
u'album.getVisitors': {
    u'name': u'album.getVisitors', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The ID of the album to get the latest visitors for.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 10, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the album latest visitors.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<visits count="10" per_page="10" pages="3" page="1" total="26">\n  <anonymous visited_at="1203604449" visits="3"/>\n  <visit user_id="12345" username="John" visited_at="1203605881" first_visit_at="1203603831" visits="2"/>\n  <visit user_id="12346" username="Bill" visited_at="1203604899" first_visit_at="1203604899" visits="1"/>\n  <visit user_id="12347" username="Tom" visited_at="1203603865" first_visit_at="1203603865" visits="1"/>\n  (...)\n</visits>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'network.docs.getRecent': {
    u'name': u'network.docs.getRecent', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'hours', u'value': u'Only return documents published since the given hours. If ommited, the timeframe is set to the last visit time for each network member. The maximum value is 744 (31 days).'
            }
            , {
        'required': 0, u'name': u'limit', u'value': u'The number of documents to show for each member. Default is 5, maximum is 10'
            }
            , {
        'required': 0, u'name': u'relation', u'value': u'Only return the members matching this relation :    <ul>    <li>0: everyone</li>    <li>1: just family</li>    <li>2: just friends</li>    <li>3: friends &amp; family</li>    <li>4: contacts</li>  </ul>'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>dates</code>, <code>count</code>, <code>geo</code>, <code>medias</code>, <code>original</code>, <code>owner</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'count', u'value': u'The number of documents to return. (Default is 50, maximum is 100)'
            }
            ], u'title': u"Return recent uploads of the calling user's network", u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<docs count="12" show="5">\n  <doc doc_id="394926" media="photo" license="0" title="test de photo">\n    <owner user_id="295"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n  </doc>\n  <doc doc_id="3611" media="photo" license="11" title="110693">\n    <owner user_id="2787"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n  </doc>\n  (...)\n</docs>', u'permissions': []
        }
        , u'doc.checkMD5': {
    u'name': u'doc.checkMD5', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'md5', u'value': u'The MD5 checksum to check or a comma seperated list of MD5 checksums (maximum is 20).'
            }
            ], u'title': u'Check if a doc exists in your stream using MD5.', u'notes': [{
        u'_value': u'Or, an empty response if the md5 was not found.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<docs count="5" found="2">\n  <doc md5="235e2a6828db582a8278cd2bc645790b" doc_id="12345" found="1"/>\n  <doc md5="0945c9c3e9ad7f32eeaaa0096934e281" found="0"/>\n  (...)\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'folder.albums.add': {
    u'name': u'folder.albums.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_id', u'value': u'The folder ID you wish to add albums to.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'An album ID or a comma separated list of album IDs. (List may contain a maximum of 20 IDs)'
            }
            ], u'title': u'Add one or many albums to a folder', u'notes': [{
        u'_value': u'An album is skipped when:<ul><li><code>added="0"</code>: it is already a member of this folder.</li></ul>', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'folder', u'response': u'<folder folder_id="10551" total="5" added="1" skipped="2">\n  <album album_id="12632" added="1" />\n  <album album_id="12732" added="0" />\n  <album album_id="12642" added="0" />\n</folder>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'album.orderList': {
    u'name': u'album.orderList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_ids', u'value': u'A comma separated list of your album IDs. The first ID will be the first displayed album. Missing album IDs will be displayed at the end of the list, ordered by their IDs.'
            }
            ], u'title': u'Change the order of your albums', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'folder.orderList': {
    u'name': u'folder.orderList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_ids', u'value': u'A comma separated list of your folder IDs. The first ID will be the first displayed folder. Missing folder IDs will be displayed at the end of the list, ordered by their IDs.'
            }
            ], u'title': u'Change the order of your folders', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'folder', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'folder.albums.remove': {
    u'name': u'folder.albums.remove', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_id', u'value': u'The folder ID you wish to remove a album from.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'A album ID or a comma separated list of album IDs. (List may contain a maximum of 20 IDs)'
            }
            ], u'title': u'Remove one or many albums from a folder', u'notes': [{
        u'_value': u'When all albums are removed from an folder (e.g. total=0), the folder will be automatically destroyed.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'folder', u'response': u'<folder folder_id="123" total="219" removed="2" skipped="1">\n  <album album_id="35658" removed="1"/>\n  <album album_id="35659" removed="1"/>\n  <album album_id="35660" removed="0"/>\n</folder>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'album.get': {
    u'name': u'album.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The ID of the album to get information for.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the cover: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            ], u'title': u'Get information about an album.', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            , {
        u'_value': u"Permissions are only returned on an authenticated call by the albums owner.\t <br/>\t The  <code>count.family</code>, <code>count.friend</code>, (...) indicates the number of documents visible for each part of the calling user's network.", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'album', u'response': u'<album album_id="10551" link="http://www.ipernity.com/doc/1/album/10551" \n       title="My very first album" thumbsize="75x">\n  <description>With my very best videos</description>\n  <dates created_at="1218038768" comment_at="0"/>\n  <count docs="2" visits="0" faves="0" comments="0"\n         family="1" friend="0" ff="0" public="1"/>\n  <cover doc_id="395574" w="75" h="75"\n         url="http://u1.ipernity.com/2/55/74/395574.a1dccd50.75x.jpg"/>\n  <can fave="1" comment="1" add_doc="1"/>\n  <permissions comment="3"/>\n  <you isfave="0" visits="1" last_visit_at="1218039770"/>\n</album>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'album.edit': {
    u'name': u'album.edit', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Album ID you wish to edit'
            }
            , {
        'required': 0, u'name': u'title', u'value': u'The new title for this album'
            }
            , {
        'required': 0, u'name': u'description', u'value': u'The new description for this album. (Some HTML tags are accepted)'
            }
            , {
        'required': 0, u'name': u'cover_id', u'value': u'The document ID to be used as the new cover. (Must belong to the calling user)'
            }
            ], u'title': u'Edit an album', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'<album album_id="10551" link="http://www.ipernity.com/doc/1/album/10551" title="A new title">\n  <description>and a new description</description>\n  <visibility ispublic="1" isfamily="1" isfriends="1" share="5"/>\n  <dates created_at="1218038768" comment_at="0"/>\n  <count docs="1" visits="0" faves="0" comments="0"/>\n  <cover cover_id="395557" w="75" h="75"\n         url="http://u1.ipernity.com/2/55/57/395557.e8265d4f.75x.jpg"/>\n  <permissions comment="3"/>\n</album>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.comments.get': {
    u'name': u'doc.comments.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'comment_id', u'value': u'The ID of the comment to get'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>.'
            }
            ], u'title': u'Return a comment on a document.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<comment comment_id="12568" user_id="5885" username="John"\n\t posted_at="1203605881" canreply="1" canedit="0"\n\t candelete="0" parent_id="1152">\n\t <content>A reply to this comment</content>\n\t <parent comment_id="1152" user_id="6778" username="Bill">\n\t   <content>The comment</content>\n\t </parent>\n</comment>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'api.methods.get': {
    u'name': u'api.methods.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'method', u'value': u'The name of the method to return information for.'
            }
            ], u'title': u'Return information about an API method.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'api.method', u'response': u'<method name="api.methods.get" service="api.method">\n  <authentication token="0" sign="0" post="0"/>\n  <title>Return information about an API method.</title>\n\n  <parameters>\n    <param name="api_key" required="1">Your api_key.</param>\n    <param name="method">The name of the method to return information for.</param>\n  </parameters>\n\n  <response>\n  (...)\n  </response>\n\n  <errors>\n    <error code="1" message="Method not found">The requested method was not found.</error>\n    <error code="100" label="api_key_missing" message="API Key is missing">Please add \n     the api_key parameter to this request.</error>\n    (...)\n  </errors>\n  <changelog>\n    <log date="2009-01-10" log="Method created."/>\n  </changelog>\n</method>', u'permissions': []
        }
        , u'doc.setPerms': {
    u'name': u'doc.setPerms', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to set permissions for.'
            }
            , {
        u'required': 0, u'name': u'is_public', u'value': u'Set to 1 to flag this document as public, 0 to make it private.'
            }
            , {
        u'required': 0, u'name': u'is_family', u'value': u'Set to 1 to flag this document as family.'
            }
            , {
        u'required': 0, u'name': u'is_friend', u'value': u'Set to 1 to flag this document as friend.'
            }
            , {
        u'required': 0, u'name': u'share', u'value': u'Set the privacy level with one parameter. Values are :<ul>\n<li>0 : private</li>\n<li>1 : visible to family</li>\n<li>2 : visible to friends</li>\n<li>3 : visible to friends & family</li>\n<li>4 : public</li>\n</ul>\nWhen sent, the <code>is_public</code>, <code>is_family</code> and <code>is_friend</code> flags are ignored.'
            }
            , {
        u'required': 0, u'name': u'perm_comment', u'value': u'The new permissions to comment on the document :<ul>\n<li>0: only you</li>\n<li>3: friends & family</li>\n<li>4: contacts</li>\n<li>5: every member</li>\n</ul>\n'
            }
            , {
        u'required': 0, u'name': u'perm_tag', u'value': u'The new permissions to add a tag on the document :<ul>\n<li>0: only you</li>\n<li>3: friends & family</li>\n<li>4: contacts</li>\n<li>5: every member</li>\n</ul>\n'
            }
            , {
        u'required': 0, u'name': u'perm_tagme', u'value': u'The new permissions to let a member add his personal member tag on the document :<ul>\n<li>0: only you</li>\n<li>3: friends & family</li>\n<li>4: contacts</li>\n<li>5: every member</li>\n</ul>\n'
            }
            ], u'title': u'Set permissions for a document.', u'notes': [{
        u'_value': u'At least one of the required parameters is needed. When setting the document privacy the three parameters is_public, is_friend, is_family are required - or use share.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'upload.file': {
    u'name': u'upload.file', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'file', u'value': u'The file data to import. Use a url-encoded post. <b>Do not include this parameter when signing the query</b>.'
            }
            , {
        'required': 0, u'name': u'title', u'value': u'The title for this document'
            }
            , {
        'required': 0, u'name': u'description', u'value': u'The description for this document. (You may use some HTML tags)'
            }
            , {
        u'required': 0, u'name': u'created_at', u'value': u'Creation date. Override creation date from EXIF'
            }
            , {
        'required': 0, u'name': u'license', u'value': u'The license code for this document.'
            }
            , {
        u'required': 0, u'name': u'is_public', u'value': u'Set to 1 to flag this document as public, 0 to make it private.'
            }
            , {
        u'required': 0, u'name': u'is_family', u'value': u'Set to 1 to flag this document as family.'
            }
            , {
        u'required': 0, u'name': u'is_friend', u'value': u'Set to 1 to flag this document as friend.'
            }
            , {
        u'required': 0, u'name': u'safety', u'value': u'Safety level. Possible values are :  \t   <ul>\t   <li>1 : document suitable for all audience</li>\t   <li>2 : document not suitable for all audience</li>\t   <li>3 : document suitable for adults only</li>\t   </ul>'
            }
            , {
        'required': 0, u'name': u'keywords', u'value': u'Add some optional keyword tags.'
            }
            , {
        'required': 0, u'name': u'album_id', u'value': u'Add this doc to an album ID.'
            }
            , {
        'required': 0, u'name': u'member_ids', u'value': u'A comma separated list of user IDs. Add member tags to this doc.'
            }
            , {
        u'required': 0, u'name': u'perm_comment', u'value': u'The permissions to comment on the document.'
            }
            , {
        u'required': 0, u'name': u'perm_tag', u'value': u'The permissions to add a tag on the document.'
            }
            , {
        u'required': 0, u'name': u'perm_tagme', u'value': u'The permissions to let a member add his personal member tag on the document.'
            }
            , {
        u'required': 0, u'name': u'lng', u'value': u'Longitude of document, decimal form e.g. 43.6667. Override longitude from EXIF'
            }
            , {
        u'required': 0, u'name': u'lat', u'value': u'Latitude of document, decimal form e.g. 6.9234. Override latitude from EXIF'
            }
            , {
        u'required': 0, u'name': u'dir', u'value': u'Orientation of document. Override oritentation from EXIF.  \t   <ul>\t   <li>1 : Up orientation</li>\t   <li>3 : Down (180\xb0 rotation)\t   <li>6 : Left orientation (90\xb0 counter clockwise)</li>\t   <li>8 : Right orientation (90\xb0 clockwise)</li>\t   </ul>'
            }
            , {
        u'required': 0, u'name': u'async', u'value': u"Wait (0) or don't wait (1) for doc to be complete"
            }
            ], u'title': u'Upload a new file.', u'notes': [{
        u'_value': u"You may try this method live without providing a file. We'll add a bulk file for you.    To force creation of a doc without geolocation, set longitude and latitude to -999.", u'for': u'params'
            }
            , {
        u'_value': u'<p>Once the upload is complete, use the <a href="/help/api/method/upload.checkTickets">upload.checkTickets</a> method to check when the documents have been processed.</p>', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'safety': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'upload', u'response': u'<ticket>12345445</ticket>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'test.hello': {
    u'name': u'test.hello', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            ], u'title': u'Hello world!', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'test', u'response': u'<hello>hello world!</hello>', u'permissions': u''
        }
        , u'faves.albums.add': {
    u'name': u'faves.albums.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'album_id', u'value': u'The album ID to add to your faves'
            }
            ], u'title': u'Add an album to your faves', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'faves', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'auth.checkToken': {
    u'name': u'auth.checkToken', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'auth_token', u'value': u'The authentication token to check.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'pref (see <a href="/help/api/method/user.pref.get">user.pref.get</a>)'
            }
            ], u'title': u'Check a token validity.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'auth', u'response': u'<auth>\n  <token>12345-a0b1c2d3e4f5</token>\n  <perms doc="write" blog="none" network="read" profile="read"/>\n  <user user_id="1234" username="Superman" realname="Kal-El"/>\n</auth>', u'permissions': []
        }
        , u'doc.getVisitors': {
    u'name': u'doc.getVisitors', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the latest visitors for.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 10, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the document latest visitors.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<visits count="10" per_page="10" pages="3" page="1" total="26">\n  <anonymous visited_at="1203604449" visits="3"/>\n  <visit user_id="12345" username="John" visited_at="1203605881" first_visit_at="1203603831" visits="2"/>\n  <visit user_id="12346" username="Bill" visited_at="1203604899" first_visit_at="1203604899" visits="1"/>\n  <visit user_id="12347" username="Tom" visited_at="1203603865" first_visit_at="1203603865" visits="1"/>\n  (...)\n</visits>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'auth.getFrob': {
    u'name': u'auth.getFrob', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            ], u'title': u'Ask for a Frob.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 1
            }
            , u'service': u'auth', u'response': u'<auth>\n  <frob>12345-a0b1c2d3e4f5</frob>\n</auth>', u'permissions': []
        }
        , u'account.getQuota': {
    u'name': u'account.getQuota', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            ], u'title': u'Return the calling user upload quota.', u'notes': [{
        u'_value': u'Only the universe is infinite. This is why an "unlimited" upload limit has an internal 10 Gig limit, automatically upgraded when reached.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'account', u'response': u'<quota user_id="1234" is_pro="1">\n  <upload unlimited="1">\n    <max  bytes="10737418240" kb="10485760" mb="10240"    percent="100" seconds="7200"/>\n    <used bytes="262144000"   kb="256000"   mb="250"      percent="3"   seconds="125"/>\n    <left bytes="10475274240" kb="10229760" mb="9990"     percent="97"  seconds="7075"/>\n  </upload>\n  <maxfilesize>\n    <photo bytes="104857600" kb="102400" mb="100"/>\n    <audio bytes="104857600" kb="102400" mb="100"/>\n    <video bytes="104857600" kb="102400" mb="100"/>\n    <other bytes="104857600" kb="102400" mb="100"/>\n  </maxfilesize>\n  <albums max="2048" created="32" left="2016">\n</quota>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'group.docs.add': {
    u'name': u'group.docs.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'group_id', u'value': u'The group ID you wish to add documents in.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'A document ID or a comma separated list of document IDs. (List may contain a maximum of 20 IDs)'
            }
            ], u'title': u'Add one or many docs to a group', u'notes': [{
        u'_value': u'A document is skipped (marked added="0") when it is already a member of this group. A document is marked as pending when it needs to be approved by the group moderators.<br/>When a doc is marked added="0" and pending="1", it means the doc has been added previously and is still waiting for approval.<br/>Document <code>error</code> codes:<ul>  <li><code>error="1"</code>: The document has been previously added to the maximum allowed groups.</li>  <li><code>error="2"</code>: The document type (photo/audio/video/other) does not match the group restrictions</li></ul>', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'group', u'response': u'<group group_id="10551" total="552" added="2" skipped="2" pending="2">\n  <doc doc_id="396419" added="1" pending="0" error="0"/>\n  <doc doc_id="396414" added="1" pending="1" error="0"/>\n  <doc doc_id="396413" added="0" pending="1" error="0"/>\n  <doc doc_id="396433" added="0" pending="0" error="1"/>\n</group>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'upload.replace': {
    u'name': u'upload.replace', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'file', u'value': u'The file data. Use a url-encoded post. <b>Do not include this parameter when signing the query</b>.'
            }
            , {
        'required': 0, u'name': u'doc_id', u'value': u'The document ID to be replaced with this file.'
            }
            , {
        'required': 0, u'name': u'async', u'value': u"Wait (0) or don't wait (1) for doc to be complete"
            }
            ], u'title': u'Replace a file.', u'notes': [{
        u'_value': u'Once the upload is complete, use the <a href="/help/api/method/upload.checkTickets">upload.checkTickets</a> method to check when the documents have been processed.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'upload', u'response': u'<ticket>12345445-98829</ticket>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'faves.albums.remove': {
    u'name': u'faves.albums.remove', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'album_id', u'value': u'The album ID to remove from your faves'
            }
            ], u'title': u'Remove an album from your faves', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'faves', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'album.docs.setList': {
    u'name': u'album.docs.setList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Album ID you wish to set its document list.'
            }
            , {
        u'required': 1, u'name': u'doc_ids', u'value': u'A comma separated list of document IDs. This list of documents will replace the album existing list. Document will appear in the album the order sent.'
            }
            , {
        u'required': 1, u'name': u'cover_id', u'value': u'The document ID to use as the album cover. This document must belong to the doc_ids list.'
            }
            ], u'title': u'Replace all the documents and the cover of an album', u'notes': [{
        u'_value': u'A document is skipped when:<ul><li><code>added="0"</code>: it is already a member of this album.</li><li><code>error="X"</code>: there was an error when adding the document to this album.</li></ul>Document <code>error</code> codes:<ul>  <li><code>error="1"</code>: The document has been previously added in the maximum allowed albums.</li></ul>', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'<album album_id="123" cover_id="1235659" total="219" added="217" skipped="2">\n  <doc doc_id="1235658" added="1" error="0"/>\n  <doc doc_id="1235659" added="1" error="0"/>\n  <doc doc_id="1235660" added="0" error="1"/>\n  <doc doc_id="1256852" added="0" error="0"/>\n  (...)\n</album>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'auth.getToken': {
    u'name': u'auth.getToken', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'frob', u'value': u'The frob.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'pref (see <a href="/help/api/method/user.pref.get">user.pref.get</a>)'
            }
            ], u'title': u'Returns the auth token for the given frob', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 1
            }
            , u'service': u'auth', u'response': u'<auth>\n  <token>12345-a0b1c2d3e4f5</token>\n  <permissions doc="write" blog="none" network="read" profile="read"/>\n  <user user_id="1234" username="Superman" realname="Kal-El"/>\n</auth>', u'permissions': []
        }
        , u'network.autocomplete': {
    u'name': u'network.autocomplete', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'query', u'value': u'Return the member usernames matching this query. The search is case insensitive.'
            }
            , {
        'required': 0, u'name': u'anywhere', u'value': u'By default the search matches username words boundaries. Setting anywhere to 1 will perform a search anywhere in the word.'
            }
            , {
        'required': 0, u'name': u'relation', u'value': u'Only return the members matching this relation :    <ul>    <li>0: everyone</li>    <li>1: just family</li>    <li>2: just friends</li>    <li>3: friends &amp; family</li>    <li>4: contacts</li>  </ul>'
            }
            ], u'title': u'Return the members matching a sub-query.', u'notes': [{
        u'_value': u'The network autocompleter only returns the first 500 results. Results must be cached. When the <code>complete</code> flag is set it means there wont be new results for queries starting by the given query.', u'for': u'params'
            }
            , {
        u'_value': u'<code>network.autocomplete</code> is specificly designed for a formular autocomplete list. This is why this method only returns the minimum data.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'network', u'response': None, u'permissions': {
        u'network': u'read'
            }
            
        }
        , u'group.get': {
    u'name': u'group.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'group_id', u'value': u'The Group ID (or Group Alias) to get details about.'
            }
            , {
        'required': 0, u'name': u'lang', u'value': u'The language code of the group title and description to fetch. If not specified, the calling user language or the browser language will be used by default.'
            }
            ], u'title': u'Get details about a group.', u'notes': [{
        u'_value': u'<p>The <code>visibility.ispublic</code> property indicates:<ul>  <li><code>ispublic="1"</code> : the group is public and open to everyone</li>  <li><code>ispublic="2"</code> : the group is public, invitation only</li>  <li><code>ispublic="0"</code> : the group is private</li></ul></p><p>The quota only applies on docs. New docs are moderated if <code>quota.moderated</code> is set to 1.<br/>A <code>quota.max="0"</code> means no quota. The quota <code>period</code> values are:<ul>  <li><code>period="d"</code> for a day</li>  <li><code>period="w"</code> for a week</li>  <li><code>period="m"</code> for a month</li>  <li><i>empty</i> for all time</li></ul>The quota limitations are only applied on members.</p>', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<group id="12345" title="A very cool group" lang="en-us"\n       link="http://www.ipernity.com/group/acoolgroup"\n       icon="http://u1.ipernity.com/p/00/01/12345.jpg">\n  <description>A cool group with a cool description</description>\n  \n  <quota moderated="0" max="10" period="w" left="3"/>\n\n  <can add_doc="1" add_topic="1" \n       accept_photo="1" accept_audio="0" accept_video="1" accept_other="0" />\n\n  <visibility ispublic="1" docs="1" topics="1"/>\n\n  <dates created_at="1218038768" \n         last_doc_at="1218048563" last_topic_at="1218048231"/>\n\n  <count members="125" docs="2563" topics="13"/>\n\n  <you isadmin="0" ismoderator="1" ismember="1" docs="255" \n       joined_at="123456585" visited_at="1218039770"/>\n</group>', u'permissions': []
        }
        , u'doc.tags.getList': {
    u'name': u'doc.tags.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to get the tags list on.'
            }
            ], u'title': u'Return the list of tags on a document.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<tags total="5">\n  <tag type="keyword" id="125652" user_id="123" tag="car!" added_at="1244198655"/>\n  <tag type="keyword" id="156658" type="keyword" user_id="123" tag="Chevrolet!" added_at="1244198655"/>\n  <tag type="keyword" id="156878" type="machine" user_id="124" tag="my:car=cool" added_at="1244198655"/>\n  <tag type="member" id="877890" user_id="123" tag="David" added_at="1244198655"/>\n  <tag type="member" id="856524" user_id="123" tag="Johnathan" added_at="1244198655"/>\n</tags>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'group.docs.remove': {
    u'name': u'group.docs.remove', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'group_id', u'value': u'The Group ID you wish to remove a document from.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'A document ID or a comma separated list of document IDs. (List may contain a maximum of 20 IDs)'
            }
            ], u'title': u'Remove one or many docs from a group', u'notes': [{
        u'_value': u'Only an administrator or a moderator of a group may remove a document not owned by himself.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'group', u'response': u'<group group_id="123" total="219" removed="2" skipped="1">\n  <doc doc_id="1235658" removed="1"/>\n  <doc doc_id="1235659" removed="1"/>\n  <doc doc_id="1235660" removed="0"/>\n</group>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'album.getList': {
    u'name': u'album.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'The ID of the user to get an album list for. (If not specified, the calling user is assumed)'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return elements matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'empty', u'value': u'Set to 1 to list empty albums.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the cover: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 100, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the albums list for a given user', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            , {
        u'_value': u"Permissions are only returned on an authenticated call by the albums owner.\t <br/>\t The  <code>count.family</code>, <code>count.friend</code>, (...) indicates the number of documents visible for each part of the calling user's network.", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'album', u'response': u'<albums total="17" per_page="2" page="1" count="2" thumbsize="75x">\n  <can create="1"/>\n  <album album_id="10551" link="http://www.ipernity.com/doc/1/album/10551" \n         title="My very first album">\n    <dates created_at="1218038768" last_comment_at="0" last_update_at="0" />\n    <count docs="2" visits="0" faves="0" comments="0" \n           family="1" friend="1" ff="1" public="1" />\n    <cover doc_id="395574" w="122" h="240"\n           url="http://u1.ipernity.com/2/55/74/395574.a1dccd50.240.jpg" />\n    <can fave="1" comment="1" />\n    <permissions comment="3" />\n  </album>\n  <album album_id="10540" link="http://www.ipernity.com/doc/1/album/10540" \n         title="Summer">\n    <visibility family="0" friend="0" ff="0" public="1" />\n    <dates created_at="1218037919" last_comment_at="0" last_update_at="0" />\n    <count docs="1" visits="0" faves="0" comments="0" />\n    <cover doc_id="395557" w="240" h="156"\n           url="http://u1.ipernity.com/2/55/57/395557.e8265d4f.240.jpg" />\n    <can fave="1" comment="1" />\n    <permissions comment="3" />\n  </album>\n</albums>', u'permissions': []
        }
        , u'folder.create': {
    u'name': u'folder.create', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'title', u'value': u'A title for this folder'
            }
            , {
        'required': 0, u'name': u'description', u'value': u'A description for this folder. (Some HTML tags are accepted)'
            }
            ], u'title': u'Create a new folder', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'folder', u'response': u'<folder folder_id="10552" link="http://www.ipernity.com/doc/1/album/10552" \n       title="My first folder">\n  <description>This is my first folder</description>\n  <dates created_at="1382543646" last_update_at="1382543646" />\n  <count albums="0" public="0" family="0" friends="0" ff="0" />\n</folder>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'album.getFaves': {
    u'name': u'album.getFaves', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The ID of the album to get the member faves list for.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 10, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of members who have faved a album.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'album', u'response': u'<faves count="10" per_page="10" pages="2" page="1" total="17">\n  <fave user_id="12345" username="John" faved_at="1203605881" />\n  <fave user_id="12346" username="Bill" faved_at="1203604899"/>\n  <fave user_id="12347" username="Tom" faved_at="1203603865" />\n  (...)\n</faves>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'tags.user.getPopular': {
    u'name': u'tags.user.getPopular', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'user_id', u'value': u'The User ID to get the list for. (if omitted, the current logged in user is assumed).'
            }
            , {
        u'required': 1, u'name': u'type', u'value': u'The type of tags to return : <code>keyword</code> or <code>member</code>. (Default is <code>keywords</code>)'
            }
            , {
        'required': 0, u'name': u'count', u'value': u'The number of tags to return. Default is 20, maximum is 100'
            }
            ], u'title': u'Get the most used tags for a given user.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'tags', u'response': u'<tags count=22" type="keyword" user_id="56685">\n  <tag id="125652" tag="car!" docs="253" posts="18"/>\n  <tag id="156658" tag="Chevrolet!" docs="220" posts="1"/>\n  (...)\n</tags>', u'permissions': []
        }
        , u'folder.edit': {
    u'name': u'folder.edit', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_id', u'value': u'The folder ID you wish to edit'
            }
            , {
        'required': 0, u'name': u'title', u'value': u'The new title for this folder'
            }
            , {
        'required': 0, u'name': u'description', u'value': u'The new description for this folder. (Some HTML tags are accepted)'
            }
            , {
        'required': 0, u'name': u'cover_id', u'value': u'The document ID to be used as the new cover. (Must belong to the calling user)'
            }
            ], u'title': u'Edit a folder', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'folder', u'response': u'<folder folder_id="11252" link="http://www.ipernity.com/doc/nikos/album/11252" title="My first folder">\n<description>This is my first folder</description>\n<dates created_at="1379929360" last_update_at="1382544142" />\n<count albums="1" public="1" family="1" friends="1" ff="1" />\n<cover label="75x" secret="516b986e" \n    url="http://u1.ipernity.com/3/34/05/403405.516b986e.75x.jpg?r1" \n    farm="1" path="/3/34/05/" ext="jpg" \n    icon="http://s.ipernity.com/icons/8.75x.png" h="75" w="75" doc_id="403405" />\n<owner user_id="10058" alias="nikos" />\n</folder>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'faves.docs.remove': {
    u'name': u'faves.docs.remove', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'doc_id', u'value': u'The doc ID to remove from your faves'
            }
            ], u'title': u'Remove a document from your faves', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'faves', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.set': {
    u'name': u'doc.set', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to edit'
            }
            , {
        'required': 0, u'name': u'title', u'value': u'The new title for this document'
            }
            , {
        'required': 0, u'name': u'description', u'value': u'The new description for this document'
            }
            ], u'title': u'Edit a document title and description.', u'notes': [{
        u'_value': u'The doc.set method can also be used to set the document geolocation, permissions, license and safety. Additional parameters are described in the <a href="/help/api/method/doc.setGeo">doc.setGeo</a>, <a href="/help/api/method/doc.setPerms">doc.setPerms</a>, <a href="/help/api/method/doc.setLicense">doc.setLicense</a> and <a href="/help/api/method/doc.setSafety">doc.setSafety</a> methods.', u'for': u'params'
            }
            , {
        u'_value': u'<ul>\n<li><code>share</code>:  0=private, 1=family, 2=friends, 3=both, 4=public</li>\n</ul>\n', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<doc doc_id="12345" title="A new title" share="0">\n  <description>Well...</description>\n</doc>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.setLicense': {
    u'name': u'doc.setLicense', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to set the license for'
            }
            , {
        u'required': 1, u'name': u'license', u'value': u'The new license ID for the document. Valid license IDs are:  \t   <ul>\t   <li>0: Copyright</li>\t   <li>1: Attribution (CC by)</li>\t   <li>3: Attribution+Non Commercial (CC by-nc)</li>\t   <li>5: Attribution+Non Deriv (CC by-nd)</li>\t   <li>7: Attribution+Non Commercial+Non Deriv (CC by-nc-nd)</li>\t   <li>9: Attribution+Share Alike (CC by-sa)</li>\t   <li>11: Attribution+Non Commercial+Share Alike (CC by-nc-sa)</li>\t   <li>255: Copyleft</li>\t   </ul>'
            }
            ], u'title': u'Set the license for a document.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'album.docs.remove': {
    u'name': u'album.docs.remove', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Album ID you wish to remove a document from.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'A document ID or a comma separated list of document IDs. (List may contain a maximum of 20 IDs)'
            }
            ], u'title': u'Remove one or many docs from an album', u'notes': [{
        u'_value': u'When all documents are removed from an album (e.g. total=0), the album will be automatically destroyed.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'<album album_id="123" total="219" removed="2" skipped="1">\n  <doc doc_id="1235658" removed="1"/>\n  <doc doc_id="1235659" removed="1"/>\n  <doc doc_id="1235660" removed="0"/>\n</album>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'faves.docs.getList': {
    u'name': u'faves.docs.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'user_id', u'value': u'The user ID to get the favorites list for. If ommited the user ID will be set as the calling user.'
            }
            , {
        'required': 0, u'name': u'owner_id', u'value': u'If set, only return docs from owner ID faved by user ID'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching a safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>owner</code>, <code>dates</code>, <code>count</code>, <code>geo</code>, <code>medias</code>, <code>original</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return a list of favorite documents for a given user', u'notes': [{
        u'_value': u"<ul>\n<li>By default, this method only returns the elements faved by <code>user_id</code> owned by others. To view <code>user_id</code>'s own faves set <code>owner_id</code> equal to <code>user_id</code>.</li>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n", u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'faves', u'response': u'<docs total="12" per_page="20" page="1" pages="1">\n  <doc doc_id="394926" media="photo" license="0" title="Nice car"\n       isfamily="1" isfriend="0" iscontact="0">\n    <thumb label="75x" ext="jpg" w="75" h="75" url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n  </doc>\n  <doc doc_id="3611" media="photo" license="11" title="DSC110693"\n       isfamily="0" isfriend="0" iscontact="1">\n    <thumb label="75x" ext="jpg" w="75" h="75" url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n  </doc>\n  (...)\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'faves.docs.add': {
    u'name': u'faves.docs.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'doc_id', u'value': u'The doc ID to add to your faves'
            }
            ], u'title': u'Add a document to your faves', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'faves', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'user.get': {
    u'name': u'user.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'user_id', u'value': u'The User ID (or User Alias) to get information about.'
            }
            ], u'title': u'Get information about a user', u'notes': [{
        u'_value': u'The flag <code>user.is_closed="1"</code> means the user account is desactivated or temporarily closed by ipernity moderation team.\t <br/>\t The <code>realname</code> value is subject to privacy settings and may not always be displayed.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 1
            }
            , u'service': u'user', u'response': u'<user user_id="12345" is_pro="0" is_online="0" is_closed="0" tmo="-3600"\n      username="Superman" realname="Kal-El" alias="superman"\n      icon="http://u1.ipernity.com/p/AA/12/12345/userphoto.jpg"\n      link="http://www.ipernity.com/home/superman">\n  <relation isfamily="0" isfriend="1" iscontact="0" revfamily="1" revfriend="1" revcontact="0"/>\n  <location country="USA" town="Smallville" lat="43.271221739661" lng="5.3876996040344" />\n  <count docs="1235" posts="25" network="32"/>\n</user>', u'permissions': []
        }
        , u'group.getList': {
    u'name': u'group.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'The ID of the user to get an group list for. (If not specified, the calling user is assumed)'
            }
            , {
        'required': 0, u'name': u'lang', u'value': u'The language code of the group title and description to fetch. If not specified, the calling user language or the browser language will be used by default.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 100, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the groups list for a given user', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'group', u'response': u'<groups total="17" per_page="2" page="1" count="2" thumbsize="75x">\n  <group group_id="10551" \n         link="http://www.ipernity.com/group/10551" \n         icon="http://u1.ipernity.com/p/00/01/10551.jpg">\n         title="Abarth lovers">\n    <visibility ispublic="1" docs="1" topics="1"/>\n    <dates created_at="1218038768" \n           last_doc_at="1218048563" last_topic_at="1218048231"/>\n    <count members="125" docs="2563" topics="13"/>\n    <you isadmin="1" ismoderator="0" ismember="0" docs="299" \n         joined_at="123456585" visited_at="1218039770"/>\n  </group>\n  <group group_id="10552" \n         link="http://www.ipernity.com/group/10551" \n         icon="http://u1.ipernity.com/p/00/01/10551.jpg">\n         title="My very first group">\n    <visibility ispublic="1" docs="1" topics="1"/>\n    <dates created_at="1218038768" \n           last_doc_at="1218048563" last_topic_at="1218048231"/>\n    <count members="125" docs="2563" topics="13"/>\n    <you isadmin="0" ismoderator="0" ismember="1" docs="0" \n         joined_at="123456585" visited_at="1218039770"/>\n  </group>\n\n</groups>', u'permissions': []
        }
        , u'network.getList': {
    u'name': u'network.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'The user ID to get the network list for.'
            }
            , {
        'required': 0, u'name': u'relation', u'value': u'Only return users matching this relation:<ul>\n<li>0: everyone</li>\n<li>1: just family</li>\n<li>2: just friends</li>\n<li>3: friends & family</li>\n<li>4: contacts</li>\n<li>8: members you blocked</li>\n</ul>\n  This parameter is only effective when calling this method as an authenticated user (<code>user_id</code> is ommited or equal to the calling user).'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>realname</code>, <code>count</code>, <code>location</code>'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u"Return members of someone's network.", u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'network', u'response': u'<network count="50" page="1" pages="1" total="122" per_page="50">\n  <user user_id="1234" username="John B."\n        icon="http://u1.ipernity.dev/p/12/34/1234/userphoto.jpg" \n        alias="john" >\n     <relation isfamily="0" isfriend="1" iscontact="0" revfriend="0"\n               revfamily="1" revcontact="0"/>\n     <count docs="256" posts="65" network="562"/>\n  </user>\n  <user user_id="1235" username="Jim" \n        icon="http://u1.ipernity.dev/p/12/34/1235/userphoto.jpg" \n        alias="jim2008" >\n    <relation isfamily="0" isfriend="1" iscontact="0" revfriend="0"\n               revfamily="1" revcontact="0"/>\n    <count docs="2656" posts="365" network="2562"/>\n  </user>\n  (...)\n</network>', u'permissions': {
        u'network': u'read'
            }
            
        }
        , u'folder.delete': {
    u'name': u'folder.delete', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_id', u'value': u'The Id of the folder to delete.'
            }
            ], u'title': u'Delete a folder', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'folder', u'response': u'', u'permissions': {
        u'doc': u'delete'
            }
            
        }
        , u'doc.search': {
    u'name': u'doc.search', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'Return documents belonging to this user_id. If ommited the search will be performed in everyone public docs.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Specify the type of returned documents. media values are : <code>photo</code>, <code>audio</code>, <code>video</code>, <code>other</code>.'
            }
            , {
        'required': 0, u'name': u'share', u'value': u'Return the calling user documents matching this privacy level. Values are :<ul>\n<li>0: private docs</li>\n<li>1: docs visible to family</li>\n<li>2: docs visible to friends</li>\n<li>3: docs visible to friends & family</li>\n<li>4: public docs</li>\n</ul>\n  This parameter will be discarded if the specified <code>user_id</code> is not the calling user.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'text', u'value': u'Search document titles, descriptions and tags using a fulltext query. (Use +/- for boolean mode)'
            }
            , {
        'required': 0, u'name': u'tags', u'value': u'Search document tags using a comma separated list of tags. (a maximum of 20 tags is allowed)'
            }
            , {
        'required': 0, u'name': u'album_id', u'value': u'Perform the search in this album ID only.'
            }
            , {
        'required': 0, u'name': u'group_id', u'value': u'Perform the search in this group ID only.'
            }
            , {
        'required': 0, u'name': u'license', u'value': u'Return documents matching this license or a comma separated list of licenses (ex: 1,3,7). See <a href="/help/api/method/doc.setLicense">doc.setLicense</a> for more details about license IDs.'
            }
            , {
        'required': 0, u'name': u'posted_min', u'value': u'Specify a minimum posted GMT+0 timestamp.'
            }
            , {
        'required': 0, u'name': u'posted_max', u'value': u'Specify a maximum posted GMT+0 timestamp.'
            }
            , {
        'required': 0, u'name': u'created_min', u'value': u'Specify a minimum creation date (using the YYYY-MM-DD HH:MM:SS format).'
            }
            , {
        'required': 0, u'name': u'created_max', u'value': u'Specify a maximum creation date (using the YYYY-MM-DD HH:MM:SS format).'
            }
            , {
        'required': 0, u'name': u'lat', u'value': u'Center point latitude in degrees.'
            }
            , {
        'required': 0, u'name': u'lng', u'value': u'Center point longitude in degrees.'
            }
            , {
        'required': 0, u'name': u'dist', u'value': u'Radius search size in meters (5 km by default, maximum 30 km).'
            }
            , {
        'required': 0, u'name': u'sort', u'value': u"The order in which to sort returned documents. The possible sorts are : <code>relevance</code>, <code>popular</code>, <code>posted-desc</code>, <code>posted-asc</code>, ''created-desc' and 'created-asc'. The default order is <code>relevance</code>."
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>, <code>dates</code>, <code>count</code>, <code>license</code>, <code>medias</code>, <code>geo</code>, <code>original</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Search for documents.', u'notes': [{
        u'_value': u'You may not combine all search parameters. For example you may not combine <code>group_id</code> and <code>album_id</code>, or a fulltext search with a tag search.<ul>\n<li>Searching text and tags syntax :</li>\n<li><code>blue sky clouds</code> : return documents containing any of these words. Rank first the documents containing the 3 words.</li>\n<li><code>+blue +sky clouds</code> : return documents showing a "blue sky" with some possible "clouds".</li>\n<li><code>+blue +sky -clouds</code> : return documents showing a "blue sky" without any "clouds".</li>\n<li><code>"the earth is round, like an orange"</code> : search the exact phrase.</li>\n</ul>\n<ul>\n<li>The search is case-insensitive but accent-sensitive.</li>\n<li>Adding a "+", "-" or quotes will activate the boolean search mode.</li>\n</ul>\n<ul>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<docs page="1" total="51258" pages="2563" per_page="20">\n  <doc doc_id="394926" title="A nice car" license="3">\n    <owner user_id="295"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n    <dates ... if option/>\n    <original ... if option and available/>\n  </doc>\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'doc.comments.reply': {
    u'name': u'doc.comments.reply', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'comment_id', u'value': u'The ID of the comment you would like to reply to'
            }
            , {
        u'required': 1, u'name': u'content', u'value': u'The text of the reply. (Some HTML tags are accepted)'
            }
            ], u'title': u'Reply to a comment on a document.', u'notes': [{
        u'_value': u"The comment ID you're replying to is listed in the API response as the <code>parent_id</code>.", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<comment parent_id="425652" comment_id="565889" user_id="58856" posted_at="1216898438"\n\t link="http://www.ipernity.com/doc/87890/8776/comment/565889#comment565889"\n\t >\n\t <content>This is &lt;b&gt;your&lt;/b&gt; reply.</content>\n</comment>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'folder.albums.getList': {
    u'name': u'folder.albums.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_id', u'value': u'The folder ID to return the albums for.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of albums to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of albums in a folder', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'folder', u'response': u'<folder folder_id="10460">\n  <albums total="12" per_page="20" page="1" pages="1">\n    <album album_id="34926" title="test de photo">\n      <thumb label="75x" ext="jpg" w="75" h="75" \n             url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n    </album>\n    <album album_id="35611" title="110693">\n      <thumb label="75x" ext="jpg" w="75" h="75" \n             url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n    </album>\n    (...)\n  </albums>\n  <cover album_id="35574" w="75" h="75"\n         url="http://u1.ipernity.com/2/55/74/395574.a1dccd50.75x.jpg"/>\n</folder>', u'permissions': []
        }
        , u'album.setPerms': {
    u'name': u'album.setPerms', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Album ID you wish to edit'
            }
            , {
        u'required': 1, u'name': u'perm_comment', u'value': u'The new permissions to comment on the album  \t   <ul>\t   <li>0: only you</li>\t   <li>3: friends &amp; family</li>\t   <li>4: contacts</li>\t   <li>5: every member</li>\t   </ul>'
            }
            ], u'title': u'Set permissions for an album', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.tags.edit': {
    u'name': u'doc.tags.edit', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to edit the tags for.'
            }
            , {
        'required': 0, u'name': u'keywords', u'value': u'The new keyword tags to set on the document.'
            }
            , {
        'required': 0, u'name': u'members', u'value': u'The new member tags to set in the document.'
            }
            ], u'title': u'Edit (in fact replace) the tags for a document owned by the calling user.', u'notes': [{
        u'_value': u'At least one of the <code>keywords</code> or <code>members</code> parameter is required. Send the parameter with an empty value to remove the tags.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<tags added="2" dropped="0">\n  <tag type="keyword" id="125652" user_id="123" tag="car!" />\n  <tag type="member" id="856524" user_id="123" tag="Johnathan" />\n</tags>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'api.methods.getList': {
    u'name': u'api.methods.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            ], u'title': u'Return the API methods list', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'api.method', u'response': u'<methods>\n  <method name="doc.delete" service="doc">\n    <authentication token="0" sign="0" post="0"/>\n    <permissions/>\n    <title>Delete a document</title>\n  </method>\n  (...)\n  <!-- changelog -->\n\n  <changelog>\n    <log date="2008-12-01">Method created.</log>\n  </changelog>\n\n</method>', u'permissions': []
        }
        , u'album.create': {
    u'name': u'album.create', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'title', u'value': u'A title for this album'
            }
            , {
        'required': 0, u'name': u'description', u'value': u'A description for this album. (Some HTML tags are accepted)'
            }
            , {
        'required': 0, u'name': u'cover_id', u'value': u'The document Id to be used as the cover. (Must belong to the calling user)'
            }
            , {
        'required': 0, u'name': u'perm_comment', u'value': u'Who can add comments to this album. Possible values are :<ul>\n<li>0: only you</li>\n<li>1: family</li>\n<li>2: friends</li>\n<li>3: friends & family</li>\n<li>4: contacts</li>\n<li>5: everybody</li>\n</ul>\n'
            }
            ], u'title': u'Create a new album', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'<album album_id="10552" link="http://www.ipernity.com/doc/1/album/10552" \n       title="My first album">\n  <description>Comment are welcome</description>\n  <visibility family="0" friend="0" ff="0" public="1"/>\n  <dates created_at="1218038872" comment_at="0"/>\n  <count docs="1" visits="0" faves="0" comments="0"/>\n  <cover doc_id="395557" w="75" h="75"\n         url="http://u1.ipernity.com/2/55/57/395557.e8265d4f.75x.jpg"/>\n  <can fave="1" comment="1"/>\n  <permissions comment="3"/>\n</album>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'explore.docs.getRecent': {
    u'name': u'explore.docs.getRecent', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching a safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'The type of media to return. Values are : <code>photo</code>, <code>video</code>, <code>audio</code> and <code>other</code>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>, <code>dates</code>, <code>license</code>, <code>medias</code>, <code>geo</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'count', u'value': u'The number of records to return. (Count is 50 by default, maximum is 100)'
            }
            ], u'title': u'Return some recent documents posted by everyone', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'explore', u'response': u'<docs count="100">\n   <doc doc_id="394926" media="photo" license="0" title="My red car">\n    <owner user_id="28987"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n  </doc>\n  <doc doc_id="3611" media="photo" license="11" title="DSC19909">\n    <owner user_id="87287"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n  </doc>\n  (...)\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'doc.delete': {
    u'name': u'doc.delete', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to delete. This document must belong to the calling user.'
            }
            ], u'title': u'Delete a document.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'delete'
            }
            
        }
        , u'doc.comments.delete': {
    u'name': u'doc.comments.delete', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'comment_id', u'value': u'The ID of the comment you wish to delete. The calling user must be the author of the comment or the owner of the document the comment was posted on.'
            }
            ], u'title': u'Delete a comment on a document.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.notes.delete': {
    u'name': u'doc.notes.delete', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'note_id', u'value': u'The note to remove.'
            }
            ], u'title': u'Remove a note from a photo.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'post.getFaves': {
    u'name': u'post.getFaves', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'post_id', u'value': u'The ID of the post to get the member faves list for.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 10, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of members who have faved a post.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'post', u'response': u'<faves count="10" per_page="10" pages="2" page="1" total="17">\n  <fave user_id="12345" username="John" faved_at="1203605881" />\n  <fave user_id="12346" username="Bill" faved_at="1203604899"/>\n  <fave user_id="12347" username="Tom" faved_at="1203603865" />\n  (...)\n</faves>', u'permissions': {
        u'post': u'read'
            }
            
        }
        , u'doc.comments.add': {
    u'name': u'doc.comments.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to add a comment on'
            }
            , {
        u'required': 1, u'name': u'content', u'value': u'The comment text. (Some HTML tags are accepted)'
            }
            , {
        'required': 0, u'name': u'preview', u'value': u'Set this flag to 1 to preview the comment. The comment will not be added.'
            }
            ], u'title': u'Comment on a document.', u'notes': [{
        u'_value': u"You can't post twice the same comment on a given document. If this happens, the comment will be accepted but not added as a duplicate.", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<comment comment_id="565889" user_id="58856" posted_at="1216898438"\n         link="http://www.ipernity.com/doc/87890/8776/comment/565889#comment565889"\n         >\n\t <content>This is &lt;b&gt;your&lt;/b&gt; comment.</content>\n</comment>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.getList': {
    u'name': u'doc.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'user_id', u'value': u'The User ID to return the documents for.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Only return this type of media. Valid values are : <code>photo</code>, <code>video</code>, <code>audio</code>, <code>other</code>.'
            }
            , {
        'required': 0, u'name': u'share', u'value': u'Only return the documents matching a privacy level. Possible values are :  \t   <ul>\t   <li>0 : private documents</li>\t   <li>1 : documents visible to family</li>\t   <li>2 : documents visible to friends</li>\t   <li>3 : documents visible to friends &amp; family</li>\t   <li>4 : public documents</li>\t   </ul>'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching a safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>dates</code>, <code>count</code>, <code>geo</code>, <code>medias</code>, <code>original</code>, <code>md5</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u"Return the member's list of documents", u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<docs total="12" per_page="20" page="1" pages="1">\n  <doc doc_id="394926" media="photo" license="0" title="My red car" safety="1">\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n  </doc>\n  <doc doc_id="3611" media="photo" license="11" title="DSC19909" safety="1">\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n  </doc>\n  (...)\n</docs>', u'permissions': []
        }
        , u'explore.docs.homepage': {
    u'name': u'explore.docs.homepage', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>, <code>dates</code>, <code>license</code>, <code>medias</code>, <code>geo</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 5, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the homepage focus last 5 items', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'explore', u'response': u'<docs count="5">\n  <doc doc_id="394926" media="photo" license="0" title="My red car">\n    <owner user_id="28987"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n  </doc>\n  <doc doc_id="3611" media="photo" license="11" title="DSC19909">\n    <owner user_id="87287"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n  </doc>\n  (...)\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'folder.getList': {
    u'name': u'folder.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'The ID of the user to get an folder list for. (If not specified, the calling user is assumed)'
            }
            , {
        'required': 0, u'name': u'empty', u'value': u'Set to 1 to list empty folders.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the cover: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 100, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the folders list for a given user', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            , {
        u'_value': u"The <code>count.family</code>, <code>count.friend</code>, (...) indicates the number of albums visible for each part of the calling user's network.", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'folder', u'response': u'<folders total="17" per_page="2" page="1" count="2" thumbsize="75x">\n  <can create="1"/>\n  <folder folder_id="10551" link="http://www.ipernity.com/doc/1/album/10551" \n         title="My very first folder">\n    <dates created_at="1218038768" />\n    <count albums="2" family="1" friend="1" ff="1" public="1" />\n    <cover doc_id="395574" w="122" h="240"\n           url="http://u1.ipernity.com/2/55/74/395574.a1dccd50.240.jpg" />\n  </folder>\n  <folder folder_id="10540" link="http://www.ipernity.com/doc/1/album/10540" \n         title="Summer">\n    <visibility family="0" friend="0" ff="0" public="1" />\n    <dates created_at="1218037919" />\n    <count albums="1" family="1" friend="1" ff="1" public="1" />\n    <cover doc_id="395557" w="240" h="156"\n           url="http://u1.ipernity.com/2/55/57/395557.e8265d4f.240.jpg" />\n  </folder>\n</folders>', u'permissions': []
        }
        , u'album.docs.getList': {
    u'name': u'album.docs.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Album ID to return the documents for.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Only return this type of media. Valid values are : <code>photo</code>, <code>video</code>, <code>audio</code>, <code>other</code>.'
            }
            , {
        'required': 0, u'name': u'share', u'value': u'Only return the documents matching this privacy level. Possible values are :  \t   <ul>\t   <li>0 : private documents</li>\t   <li>1 : documents visible to family</li>\t   <li>2 : documents visible to friends</li>\t   <li>3 : documents visible to friends &amp; family</li>\t   <li>4 : public documents</li>\t   </ul>    This option is only available on an album owned by an authenticated calling user.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>dates</code>, <code>geo</code>, <code>medias</code>, <code>original</code>, <code>link</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of documents in an album', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'album', u'response': u'<album album_id="10460">\n  <docs total="12" per_page="20" page="1" pages="1">\n    <doc doc_id="394926" media="photo" license="0" title="test de photo" safety="1">\n      <thumb label="75x" ext="jpg" w="75" h="75" \n             url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n    </doc>\n    <doc doc_id="3611" media="photo" license="11" title="110693" safety="1">\n      <thumb label="75x" ext="jpg" w="75" h="75" \n             url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n    </doc>\n    (...)\n  </docs>\n  <cover doc_id="395574" w="75" h="75"\n         url="http://u1.ipernity.com/2/55/74/395574.a1dccd50.75x.jpg"/>\n</album>', u'permissions': []
        }
        , u'doc.getContainers': {
    u'name': u'doc.getContainers', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the containers for.'
            }
            ], u'title': u'Return all albums and groups the document belongs to.', u'notes': [{
        u'_value': u'', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<albums total="1">\n  <album album_id="10551" title="My very first album" docs="4" \n         cover="http://u1.ipernity.com/2/55/74/395574.a1dccd50.75x.jpg"\n         link="http://www.ipernity.com/doc/1/album/10551"/>\n</albums>\n\n<groups total="3" added="1" pending="1" invited="1">\n  <group group_id="170" title="Blue skies" docs="19" \n         pending="0" invited="0" \n         cover="http://u1.ipernity.com/p/AA/00/170/userphoto.jpg" \n         link="http://www.ipernity.com/group/170"/>\n\n  <group group_id="172" title="A moderated group" docs="129" \n         pending="1" invited="0"\n         cover="http://u1.ipernity.com/p/AA/00/172/userphoto.jpg" \n         link="http://www.ipernity.com/group/172"/>\n\n  <group group_id="213" title="Invitations only" docs="199" \n         pending="0" invited="1"\n         cover="http://u1.ipernity.com/p/AA/00/213/userphoto.jpg" \n         link="http://www.ipernity.com/group/213"/>\n</groups>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'album.delete': {
    u'name': u'album.delete', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Id of the album to delete.'
            }
            ], u'title': u'Delete an album', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'', u'permissions': {
        u'doc': u'delete'
            }
            
        }
        , u'group.docs.getContext': {
    u'name': u'group.docs.getContext', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'group_id', u'value': u'The Group ID which the document belongs to.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the context for. By default 10 previous and 10 next documents are returned.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'Only return documents owned by the specified User ID.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Specify the type of returned documents. media values are : <code>photo</code>, <code>audio</code>, <code>video</code>, <code>other</code>. If specified, the media type must be the same as the document <code>doc_id</code>.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'prev', u'value': u'Only return some previous (oldest) documents. (Value is from 1 to 50)'
            }
            , {
        'required': 0, u'name': u'next', u'value': u'Only return some next (newest) documents. (Value is from 1 to 50)'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra value is: <code>owner</code>.'
            }
            ], u'title': u'Get the document context in a group', u'notes': [{
        u'_value': u'<ul>\n<li>The <code>next</code> and <code>prev</code> direction refer to the group order. Moving to the previous items goes to the group first added items and moving to the next items goes to the group last added items.</li>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'group', u'response': u'<group group_id="5555" total="125" thumbsize="75x"/>\n<prev count="18">\n  <doc index="-1" doc_id="51" media="photo" title="Doc 51"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/51/51.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/51/in/group/5555" user_id="123"/>\n  <doc index="-2" doc_id="50" media="photo" title="Doc 50"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/50/50.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/50/in/group/5555" user_id="123"/>\n  (...)\n  <doc index="-18" doc_id="33" media="photo" title="Doc 68"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/33/33.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/33/in/group/5555" user_id="123"/>\n</prev>\n<doc index="0" doc_id="50" media="photo" title="Doc 50"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/50/50.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/50/in/group/5555" user_id="123"/>\n<next count="10">\n  <doc index="1" doc_id="52" media="photo" title="Doc 52"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/52/52.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/52/in/group/5555" user_id="123"/>\n  <doc index="2" doc_id="53" media="photo" title="Doc 53"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/53/53.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/53/in/group/5555" user_id="123"/>\n  (...)\n  <doc index="10" doc_id="61" media="photo" title="Doc 61"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/61/61.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/61/in/group/5555" user_id="123"/>\n</next>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'folder.get': {
    u'name': u'folder.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'folder_id', u'value': u'The ID of the folder to get information for.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the cover: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            ], u'title': u'Get information about a folder.', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            , {
        u'_value': u"The <code>count.family</code>, <code>count.friend</code>, (...) indicates the number of albums visible for each category of the member's contacts", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'folder', u'response': u'<folder folder_id="11252" link="http://www.ipernity.com/doc/nikos/album/11252" \n    title="My first folder">\n<description>This is my first folder</description>\n<dates created_at="1379929360" last_update_at="1379929360" />\n<count albums="1" public="1" family="1" friends="1" ff="1" />\n<cover label="250x" secret="c8807d4f" \n    url="http://u1.ipernity.com/3/81/52/398152.c8807d4f.250x.jpg?r1" \n    farm="1" path="/3/81/52/" ext="jpg" \n    icon="http://s.ipernity.com/icons/8.75x.png" h="250" w="250" doc_id="398152" />\n<owner user_id="10058" alias="nikos" />\n</folder>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'doc.tags.add': {
    u'name': u'doc.tags.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to add a tag on.'
            }
            , {
        'required': 0, u'name': u'keywords', u'value': u'The keyword tags to add to the document. You may add one or more keyword tags using the syntax: <code>holidays,beach</code> or <code>"blue sky",sunset</code>.'
            }
            , {
        'required': 0, u'name': u'members', u'value': u'A comma separated list of member IDs or member Web aliases. The members must belong to the calling user network.'
            }
            ], u'title': u'Add a tag to a document.', u'notes': [{
        u'_value': u'At least one of the <code>keywords</code> or <code>members</code> parameter is required.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<tags added="2" dropped="0">\n    <tag type="keyword" id="125652" user_id="123" tag="car!" />\n    <tag type="member" id="67787" user_id="123" tag="Johnathan" />\n  </tags>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.comments.edit': {
    u'name': u'doc.comments.edit', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'comment_id', u'value': u'The ID of the comment you wish to edit'
            }
            , {
        u'required': 1, u'name': u'content', u'value': u'The new comment text. (Some HTML tags are accepted)'
            }
            , {
        'required': 0, u'name': u'preview', u'value': u'Set this flag to 1 to preview the comment. The comment will not be added.'
            }
            ], u'title': u'Edit a comment on a document.', u'notes': [{
        u'_value': u'The <code>modified</code> timestamp is set only if the modification occurs 5 minutes after the creation timestamp. The original author (<code>user_id</code>) is never modified.', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<comment comment_id="565889" user_id="58856" posted_at="1216898438" modified_at="1216925451"\n         link="http://www.ipernity.com/doc/87890/8776/comment/565889#comment565889"\n         >\n\t <content>This is &lt;b&gt;my&lt;/b&gt; modified comment.</content>\n</comment>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.tags.remove': {
    u'name': u'doc.tags.remove', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to remove a tag from.'
            }
            , {
        u'required': 1, u'name': u'type', u'value': u'The type is <code>keyword</code> or <code>member</code>'
            }
            , {
        u'required': 1, u'name': u'id', u'value': u'The ID of the tag to remove.'
            }
            ], u'title': u'Remove a tag from a document.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.setGeo': {
    u'name': u'doc.setGeo', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document you wish to geolocate.'
            }
            , {
        u'required': 0, u'name': u'lng', u'value': u'Longitude of document, decimal form e.g. 43.6667. Override longitude from EXIF'
            }
            , {
        u'required': 0, u'name': u'lat', u'value': u'Latitude of document, decimal form e.g. 6.9234. Override latitude from EXIF'
            }
            ], u'title': u'Set longitude and latitude of a document.', u'notes': [{
        u'_value': u'To reset longitude and latitude, use -999 for both values.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'tags.docs.getList': {
    u'name': u'tags.docs.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'type', u'value': u'The type of tag: <code>keyword</code> or <code>member</code>.'
            }
            , {
        u'required': 1, u'name': u'id', u'value': u'The ID of the tag'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'Only return documents owned by the given user_id'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Only return this type of media. Valid values are : <code>photo</code>, <code>video</code>, <code>audio</code>, <code>other</code>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>owner</code>, <code>dates</code>, <code>medias</code>, <code>original</code>.'
            }
            , {
        'required': 0, u'name': u'sort', u'value': u'The order in which to sort returned documents. The possible sorts are : <code>popular</code>, <code>posted-desc</code>, <code>posted-asc</code>. The default order is <code>popular</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 100, maximum is 500)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of documents for a given tag', u'notes': [{
        u'_value': u'<ul>\n<li>The extra parameter <code>original</code> is only availale when requesting documents for a given <code>user_id</code>.</li>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'tags', u'response': u'<docs page="1" total="51258" pages="2563" per_page="20">\n  <doc doc_id="394926" title="A nice car" license="3">\n    <owner user_id="295"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n    <dates ... if option/>\n    <original ... if option and available/>\n  </doc>\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'doc.getMedias': {
    u'name': u'doc.getMedias', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get information for.'
            }
            ], u'title': u'Get document media urls (thumbs, medias, original,...).', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<thumbs>\n     <thumb label="75x" w="75" h="75"    \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.75x.jpg"/>\n     <thumb label="100" w="100" h="90"   \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.100.jpg"/>\n     <thumb label="240" w="240" h="120"  \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.240.jpg"/>\n     <thumb label="500" w="500" h="400"  \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.500.jpg"/>\n     <thumb label="560" w="560" h="420"  \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.560.jpg"/>\n     <thumb label="1024" secret="5dae5623" w="1024" h="900"   \n            url="http://u1.ipernity.com/1/00/01/12345.5dae5623.1024.jpg"/>\n  </thumbs>\n  <medias>\n    <media label="flv" ext="flv" w="480" h="360" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.flv"/>\n    <media label="ipod" ext="mp4" w="480" h="272" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.ipod.mp4"/>\n    <media label="mp4" ext="mp4" w="480" h="360" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.mp4"/>\n    <media label="hd" ext="mp4" w="1920" h="1080" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.hd.mp4"/>\n  </medias>\n  <players>\n    <player label="flv" type="flash" w="480" h="360"\n            url="http://www.ipernity.com/mp/12345.ac67de87.flv.swf"/>\n  </players>\n\n  <original ext="mpg" w="1024" h="900" length="120"\n            filename="my car.mpg" bytes="585654"\n            url="http://u1.ipernity.com/1/00/01/12345.253ade85.mpg"/>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'doc.get': {
    u'name': u'doc.get', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get details about.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>tags</code>, <code>notes</code>, <code>geo</code> and <code>md5</code>.'
            }
            ], u'title': u'Get details about document.', u'notes': [{
        u'_value': u'<ul>\n<li><code>share</code>:  0=private, 1=family, 2=friends, 3=both, 5=public</li>\n<li><code>media</code>: photo, audio, video or other</li>\n<li><code>permissions</code>: 0=private, 1=family, 2=friends, 3=both, 4=contacts, 5=public</li>\n</ul>\n', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<doc doc_id="12345" media="video" license="1" rotation="0" \n     title="This is my first car" safety="1"\n     link="http://www.ipernity.com/doc/christophe/12345">\n\n  <owner user_id="123" username="Christophe" realname=""/>\n\n  <description>It\'s an AUTOBIANCHI Abart</description>\n\n  <dates posted_at="1203605781" replaced_at="1203605881" \n         created="2008-01-03 11:22:00"\n         modified_at="1203683781" comment_at="1203685781"/>\n\n  <visibility ispublic="1" isfriend="0" isfamily="0" share="5" />\n\n  <permissions comment="3" tag="3" tagme="3" />\n\n  <count visits="96" faves="5" comments="15" notes="2" tags="5" albums="1" groups="0" \n         last_visit="1203683781"/>\n\n  <can fave="1" comment="1" tag="1" tagme="1" zoom="1" download="0" print="0"/>\n\n  <you isfave="1" visits="2" last_visit="1203608781"/>\n\n  <thumbs>\n     <thumb label="75x" w="75" h="75"    \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.75x.jpg"/>\n     <thumb label="100" w="100" h="90"   \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.100.jpg"/>\n     <thumb label="240" w="240" h="120"  \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.240.jpg"/>\n     <thumb label="500" w="500" h="400"  \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.500.jpg"/>\n     <thumb label="560" w="560" h="420"  \n            url="http://u1.ipernity.com/1/00/01/12345.d5ea56eb.560.jpg"/>\n     <thumb label="1024" w="1024" h="900"   \n            url="http://u1.ipernity.com/1/00/01/12345.5dae5623.1024.jpg"/>\n  </thumbs>\n  <medias>\n    <media label="flv" ext="flv" w="480" h="360" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.flv"/>\n    <media label="ipod" ext="mp4" w="480" h="272" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.ipod.mp4"/>\n    <media label="mp4" ext="mp4" w="480" h="360" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.mp4"/>\n    <media label="hd" ext="mp4" w="1920" h="1080" lenght="120"\n           url="http://u1.ipernity.com/1/00/01/12345.5dae5623.hd.mp4"/>\n  </medias>\n  <original ext="mpg" w="1024" h="900" length="120"\n            filename="my car.mpg" bytes="585654"\n            url="http://u1.ipernity.com/1/00/01/12345.253ade85.mpg"/>\n\n  <geo lat="000" lng="000" loc_id="234" location="Paris"/>\n\n  <tags total="5">\n    <tag tag_id="125652" type="keyword" user_id="123" keyword="car" title="car!" />\n    <tag tag_id="156658" type="keyword" user_id="123" keyword="chevrolet" title="Chevrolet!" />\n    <tag tag_id="877890" type="member" user_id="123" member_id="123" title="David" />\n    <tag tag_id="856524" type="member" user_id="123" member_id="568" title="Johnathan" />\n  </tags>\n\n  <notes total="2">\n    <note note_id="13" user_id="586586" username="Fred" x="40" y="50" \n          w="100" h="110">I love the Starsky &amp; Hutch painting</note>\n    <note note_id="28" user_id="236569" username="Tom" x="80" y="30" \n          w="50" h="50">Nice \n                        car</note>\n  </notes>\n  \n</doc>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'album.docs.add': {
    u'name': u'album.docs.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The album ID you wish to add documents in.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'A document ID or a comma separated list of document IDs. (List may contain a maximum of 20 IDs)'
            }
            ], u'title': u'Add one or many docs to an album', u'notes': [{
        u'_value': u'A document is skipped when:<ul><li><code>added="0"</code>: it is already a member of this album.</li><li><code>error="X"</code>: there was an error when adding the document to this album.</li></ul><br/>Document <code>error</code> codes:<ul>  <li><code>error="1"</code>: The document has been previously added in the maximum allowed albums.</li></ul>', u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'album', u'response': u'<album album_id="10551" total="5" added="1" skipped="2">\n  <doc doc_id="396419" added="1" error="0"/>\n  <doc doc_id="396414" added="0" error="0"/>\n  <doc doc_id="396413" added="0" error="1"/>\n</album>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.notes.edit': {
    u'name': u'doc.notes.edit', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'note_id', u'value': u'The ID of the note you wish to edit.'
            }
            , {
        u'required': 1, u'name': u'content', u'value': u'The new note text. (Some HTML tags are accepted)'
            }
            , {
        u'required': 1, u'name': u'x', u'value': u'The left coordinate of the note.'
            }
            , {
        u'required': 1, u'name': u'y', u'value': u'The top coordinate of the note.'
            }
            , {
        u'required': 1, u'name': u'w', u'value': u'The width of the note.'
            }
            , {
        u'required': 1, u'name': u'h', u'value': u'The height of the note.'
            }
            , {
        'required': 0, u'name': u'preview', u'value': u'Set this flag to 1 to preview the note. The note will not be added.'
            }
            ], u'title': u'Edit a note on a photo.', u'notes': [{
        u'_value': u'The note coordinates are expressed in pixels. See <a href="/help/api/method/doc.notes.add">doc.notes.add</a>.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<note note_id="58856" user_id="58565" posted_at="1216898438" x="10" y="12" w="22" h="33">Your note</note>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'explore.docs.getPopular': {
    u'name': u'explore.docs.getPopular', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching a safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'The type of media to return. Values are : <code>photo</code> and <code>video</code>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>, <code>dates</code>, <code>license</code>, <code>medias</code>, <code>geo</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 50)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the week most popular documents', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'explore', u'response': u'<docs total="12" per_page="20" page="1" pages="1">\n  <doc doc_id="394926" media="photo" license="0" title="My red car">\n    <owner user_id="28987"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n  </doc>\n  <doc doc_id="3611" media="photo" license="11" title="DSC19909">\n    <owner user_id="87287"/>\n    <thumb label="75x" ext="jpg" w="75" h="75" \n           url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n  </doc>\n       (...)\n</docs>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'tags.user.getList': {
    u'name': u'tags.user.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'user_id', u'value': u'The User ID to get the list for. (if omitted, the current logged in user is assumed).'
            }
            , {
        u'required': 1, u'name': u'type', u'value': u'The type of tags to return : <code>keyword</code> or <code>member</code>. (Default is <code>keywords</code>)'
            }
            , {
        'required': 0, u'name': u'count', u'value': u'The number of tags to return. Default is 100, maximum is 1000'
            }
            ], u'title': u'Get the tags list for a given user.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'tags', u'response': u'<tags count=22" type="keywords" user_id="56685">\n  <tag type="keyword" id="125652" tag="car!" />\n  <tag type="keyword" id="156658" tag="Chevrolet!" />\n  (...)\n</tags>', u'permissions': []
        }
        , u'faves.albums.getList': {
    u'name': u'faves.albums.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'user_id', u'value': u'The user ID to get the favorites list for. If ommited the user ID will be set as the calling user.'
            }
            , {
        'required': 0, u'name': u'owner_id', u'value': u'If set, only return albums from owner ID faved by user ID'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return a list of favorite albums for a given user', u'notes': [{
        u'_value': u"<ul>\n<li>By default, this method only returns the elements faved by <code>user_id</code> owned by others. To view <code>user_id</code>'s own faves set <code>owner_id</code> equal to <code>user_id</code>.</li>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n", u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'faves', u'response': u'<albums total="17" per_page="2" page="1" count="2">\n  <album album_id="10551" link="http://www.ipernity.com/doc/1/album/10551" \n         title="My very first album" user_id="1">\n    <dates created_at="1220629307" last_comment_at="0" last_update_at="1220629354"/>\n    <count docs="2" visits="0" faves="0" comments="0" />\n    <cover cover_id="395574" w="122" h="240"\n           url="http://u1.ipernity.com/2/55/74/395574.a1dccd50.240.jpg" />\n    <can fave="1" comment="1"/>\n  </album>\n  <album album_id="10540" link="http://www.ipernity.com/doc/2/album/10540" \n         title="Summer" user_id="2">\n    <dates created_at="1176292271" last_comment_at="1176725507" last_update_at="1176725940"/>\n    <count docs="1" visits="0" faves="0" comments="0" />\n    <cover doc_id="395557" w="75" h="75"\n           url="http://u1.ipernity.com/2/55/57/395557.e8265d4f.240.jpg" />\n    <can fave="1" comment="1"/>\n  </album>\n</albums>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'test.echo': {
    u'name': u'test.echo', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'echo', u'value': u'Some text we will echo back to you.'
            }
            ], u'title': u'A simple echo test.', u'notes': [{
        u'_value': u'This method echoes to you any given parameter. The parameter echo is only given as an example.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'test', u'response': u'<echo>yes, it worked</echo>', u'permissions': u''
        }
        , u'doc.notes.add': {
    u'name': u'doc.notes.add', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the photo you wish to add a note on.'
            }
            , {
        u'required': 1, u'name': u'content', u'value': u'The note text. (Some HTML tags are accepted)'
            }
            , {
        'required': 0, u'name': u'member_id', u'value': u'The user ID associated to this note.'
            }
            , {
        u'required': 1, u'name': u'x', u'value': u'The left coordinate of the note.'
            }
            , {
        u'required': 1, u'name': u'y', u'value': u'The top coordinate of the note.'
            }
            , {
        u'required': 1, u'name': u'w', u'value': u'The width of the note.'
            }
            , {
        u'required': 1, u'name': u'h', u'value': u'The height of the note.'
            }
            , {
        'required': 0, u'name': u'preview', u'value': u'Set this flag to 1 to preview the note. The note will not be added.'
            }
            ], u'title': u'Add a note to a photo.', u'notes': [{
        u'_value': u"The note coordinates are expressed in pixels. Notes are shown normally on the 560 pixel image size. If the coordinates don't match with the photo dimensions, the note will be placed at <code>x=0, y=0, w=50, h=50</code>.    When associating a member ID to a note, the <code>content</code> is not required.", u'for': u'params'
            }
            ], u'authentication': {
        u'token': 1, u'post': 1, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<note note_id="58856" user_id="58565" posted_at="1216898438" x="10" y="12" w="22" h="33">Your note</note>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'doc.getFaves': {
    u'name': u'doc.getFaves', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the member faves list for.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 10, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of members who have faved a document.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<faves count="10" per_page="10" pages="2" page="1" total="17">\n  <fave user_id="12345" username="John" faved_at="1203605881" />\n  <fave user_id="12346" username="Bill" faved_at="1203604899"/>\n  <fave user_id="12347" username="Tom" faved_at="1203603865" />\n  (...)\n</faves>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'group.docs.getList': {
    u'name': u'group.docs.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'group_id', u'value': u'The Group ID to return the documents for.'
            }
            , {
        'required': 0, u'name': u'user_id', u'value': u'Only return documents owned by the specified User ID.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Specify the type of returned documents. media values are : <code>photo</code>, <code>audio</code>, <code>video</code>, <code>other</code>. If specified, the media type must be the same as the document <code>doc_id</code>.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information to include in each records. Extra values are: <code>owner</code>, <code>dates</code>, <code>geo</code>, <code>medias</code>, <code>original</code>.'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for the thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the list of documents in a group', u'notes': [{
        u'_value': u'Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'group', u'response': u'<group group_id="10460">\n  <docs total="12" per_page="20" page="1" pages="1">\n    <doc doc_id="394926" media="photo" license="0" title="test de photo">\n      <thumb label="75x" ext="jpg" w="75" h="75" url="http://u1.ipernity.com/2/49/26/394926.e831d113.75x.jpg"/>\n    </doc>\n    <doc doc_id="3611" media="photo" license="11" title="110693">\n      <thumb label="75x" ext="jpg" w="75" h="75" url="http://u1.ipernity.com/1/36/11/3611.236f34e9.75x.jpg"/>\n    </doc>\n    (...)\n  </docs>\n</group>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'explore.groups.getRandom': {
    u'name': u'explore.groups.getRandom', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'count', u'value': u'The number of groups to return. (Default is 10, maximum is 50)'
            }
            ], u'title': u'Return some random interesting groups', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'explore', u'response': u'<groups count="10">\n  <group group_id="125" title="Abarth lovers" \n         link="http://www.ipernity.com/group/acoolgroup"\n         icon="http://u1.ipernity.com/p/00/01/125.jpg">\n    <count members="125" docs="2563" topics="13"/>\n    <dates created_at="1218038768" \n           last_doc_at="1218048563" last_topic_at="1218048231"/>\n    <visibility ispublic="1" docs="1" topics="1"/>\n  </group>\n   <group group_id="126" title="Kitty Club" \n         link="http://www.ipernity.com/group/kitty"\n         icon="http://u1.ipernity.com/p/00/01/126.jpg">\n    <count members="1325" docs="25563" topics="636"/>\n    <dates created_at="1218048748" \n           last_doc_at="1218348462" last_topic_at="1218044233"/>\n    <visibility ispublic="1" docs="1" topics="1"/>\n  </group>\n  (...)\n</groups>', u'permissions': []
        }
        , u'doc.getContext': {
    u'name': u'doc.getContext', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the context for. By default 10 previous and 10 next documents are returned'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Specify the type of returned documents. media values are : <code>photo</code>, <code>audio</code>, <code>video</code>, <code>other</code>.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching this safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'prev', u'value': u'Only return some previous (oldest) documents. (Value is from 1 to 50)'
            }
            , {
        'required': 0, u'name': u'next', u'value': u'Only return some next (newest) documents. (Value is from 1 to 50)'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            ], u'title': u'Get the document context in docstream', u'notes': [{
        u'_value': u'<ul>\n<li>The <code>next</code> and <code>prev</code> direction refer to the stream posted date order. Moving to the previous items goes to the stream oldest items and moving to the next items goes to the stream recent items.</li>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<prev count="18">\n  <doc index="-1" doc_id="51" media="photo" title="Doc 51" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/51/51.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/51" user_id="123"/>\n  <doc index="-2" doc_id="50" media="photo" title="Doc 50"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/50/50.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/50" user_id="123"/>\n  (...)\n  <doc index="-18" doc_id="33" media="photo" title="Doc 68" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/33/33.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/33" user_id="123"/>\n</prev>\n<doc index="0" doc_id="50" media="photo" title="Doc 50" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/50/50.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/50" user_id="123"/>\n<next count="10">\n  <doc index="1" doc_id="52" media="photo" title="Doc 52" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/52/52.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/52" user_id="123"/>\n  <doc index="2" doc_id="53" media="photo" title="Doc 53" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/53/53.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/53" user_id="123"/>\n  (...)\n  <doc index="10" doc_id="61" media="photo" title="Doc 61" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/61/61.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/61" user_id="123"/>\n</next>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'upload.checkTickets': {
    u'name': u'upload.checkTickets', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'tickets', u'value': u'A comma delimited list of upload tickets. (A list of 50 tickets is a maximum).'
            }
            ], u'title': u'Check the status of one or more upload tickets.', u'notes': [{
        u'_value': u"<p>The global <code>eta</code> (estimated time of arrival) value represents the number of seconds left to complete the tickets. Each ticket has it's own <code>eta</code>. Please do not query unecessary tickets such as done tickets or before it's eta is supposed to be 0.</p><p>Once the tickets have been processed, you may redirect to the following url : <code>http://www.ipernity.com/doc/(user_id)/uploaded?doc_id1,doc_id2,doc_id3,...</code></p>", u'for': u'response'
            }
            ], u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'upload', u'response': u'<tickets count="4" done="2" invalid="1" left="1" eta="120">\n  <ticket id="712218" done="1" invalid="0" doc_id="5412" eta="0"/>\n  <ticket id="712219" done="0" invalid="1" eta="0"/>\n  <ticket id="712310" done="1" invalid="0" doc_id="1235" eta="0"/>\n  <ticket id="712311" done="0" invalid="0" eta="120"/>\n</tickets>', u'permissions': {
        u'doc': u'write'
            }
            
        }
        , u'post.getVisitors': {
    u'name': u'post.getVisitors', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'post_id', u'value': u'The ID of the post to get the latest visitors for.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 10, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the post latest visitors.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<visits count="10" per_page="10" pages="3" page="1" total="26">\n  <anonymous visited_at="1203604449" visits="3"/>\n  <visit user_id="12345" username="John" visited_at="1203605881" first_visit_at="1203603831" visits="2"/>\n  <visit user_id="12346" username="Bill" visited_at="1203604899" first_visit_at="1203604899" visits="1"/>\n  <visit user_id="12347" username="Tom" visited_at="1203603865" first_visit_at="1203603865" visits="1"/>\n  (...)\n</visits>', u'permissions': {
        u'post': u'read'
            }
            
        }
        , u'doc.getPerms': {
    u'name': u'doc.getPerms', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the permissions for.'
            }
            ], u'title': u'Return permissions for a document.', u'notes': u'', u'authentication': {
        u'token': 1, u'post': 0, u'sign': 1
            }
            , u'service': u'doc', u'response': u'<visibility ispublic="1" isfriend="0" isfamily="0"/>\n<permissions permcomment="3" permtag="3" permtagme="3" />\n<usage canfave="1" cancomment="1" cantag="1" cantagme="1" canzoom="1" candownload="0" canprint="0"/>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'doc.comments.getList': {
    u'name': u'doc.comments.getList', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the comment list for'
            }
            , {
        'required': 0, u'name': u'extra', u'value': u'A comma seprarated list of extra information. Extra parameters are: <code>owner</code>.'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of records to return on each page. (Default is 100, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Return the comments on a document.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'doc', u'response': u'<comments doc_id="588568" total="2" count="2" per_page="100" page="1" pages="1">\n  <comment comment_id="12568" user_id="5885" username="John" \n           posted_at="1203605881">\n\t   <content>The first comment</content>\n  </comment>\n  <comment comment_id="12569" parent_id="12568" user_id="5886" username="Jim" \n           posted_at="1203605982" modified_at="1203606243">\n\t   <content>Yes, I can see this ;)</content>\n  </comment>\n</comments>', u'permissions': {
        u'doc': u'read'
            }
            
        }
        , u'group.search': {
    u'name': u'group.search', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        'required': 0, u'name': u'text', u'value': u'Search group titles and descriptions in fulltext. (Use +/- for boolean mode)'
            }
            , {
        'required': 0, u'name': u'lang', u'value': u'The language code of the group title and description to fetch. If not specified, the calling user language or the browser language will be used by default.'
            }
            , {
        'required': 0, u'name': u'sort', u'value': u'The order in which to sort returned groups:  \t   <ul>\t   <li><code>relevance</code>: sort by fulltext relevance. (This is the default).</li>\t   <li><code>created-desc</code>: sort by creation date newest first.</li>\t   <li><code>created-asc</code>: sort by creation date oldest first.</li>\t   </ul>'
            }
            , {
        'required': 0, u'name': u'per_page', u'value': u'The number of docs to return on each page. (Default is 20, maximum is 100)'
            }
            , {
        'required': 0, u'name': u'page', u'value': u'The page of results to return.'
            }
            ], u'title': u'Search for a group.', u'notes': u'', u'authentication': {
        u'token': 0, u'post': 0, u'sign': 0
            }
            , u'service': u'group', u'response': u'<groups page="1" total="5125" pages="256" per_page="20">\n  <group group_id="125" title="Abarth lovers" \n         link="http://www.ipernity.com/group/acoolgroup"\n         icon="http://u1.ipernity.com/p/00/01/125.jpg">\n    <count members="125" docs="2563" topics="13"/>\n    <dates created_at="1218038768" \n           last_doc_at="1218048563" last_topic_at="1218048231"/>\n    <visibility ispublic="1" docs="1" topics="1"/>\n  </group>\n   <group group_id="126" title="Kitty Club" \n         link="http://www.ipernity.com/group/kitty"\n         icon="http://u1.ipernity.com/p/00/01/126.jpg">\n    <count members="1325" docs="25563" topics="636"/>\n    <dates created_at="1218048748" \n           last_doc_at="1218348462" last_topic_at="1218044233"/>\n    <visibility ispublic="1" docs="1" topics="1"/>\n  </group>\n  (...)\n</groups>', u'permissions': []
        }
        , u'album.docs.getContext': {
    u'name': u'album.docs.getContext', u'parameters': [{
        u'required': 1, u'name': u'api_key', u'value': u'Your api_key.'
            }
            , {
        u'required': 1, u'name': u'album_id', u'value': u'The Album ID which the document belongs to.'
            }
            , {
        u'required': 1, u'name': u'doc_id', u'value': u'The ID of the document to get the context for. By default 10 previous and 10 next documents are returned.'
            }
            , {
        'required': 0, u'name': u'media', u'value': u'Specify the type of returned documents. media values are : <code>photo</code>, <code>audio</code>, <code>video</code>, <code>other</code>. If specified, the media type must be the same as the document <code>doc_id</code>.'
            }
            , {
        'required': 0, u'name': u'safesurf', u'value': u'Only return the documents matching a safety level. See <a href="/help/api/method/doc.setSafety">doc.setSafety</a>.'
            }
            , {
        'required': 0, u'name': u'prev', u'value': u'Only return some previous (oldest) documents. (Value is from 1 to 50)'
            }
            , {
        'required': 0, u'name': u'next', u'value': u'Only return some next (newest) documents. (Value is from 1 to 50)'
            }
            , {
        'required': 0, u'name': u'thumbsize', u'value': u'Choose your prefered size for thumbnails: <code>75x, 100, 240, 250x, 500, 560, 640, 800, 1024, 1600 or 2048</code>. (Value is <code>75x</code> by default)'
            }
            ], u'title': u'Get the document context in an album', u'notes': [{
        u'_value': u'<ul>\n<li>The <code>next</code> and <code>prev</code> direction refer to the album order. Moving to the previous items goes to the album first added items and moving to the next items goes to the album added last items.</li>\n<li>Access to thumbnail size greater than <code>800</code> pixels depends on user preferences.</li>\n</ul>\n', u'for': u'params'
            }
            ], u'authentication': {
        u'token': 0, u'safety': 1, u'post': 0, u'sign': 0
            }
            , u'service': u'album', u'response': u'<album album_id="5555" total="125" thumbsize="75x"/>\n<prev count="18">\n  <doc index="-1" doc_id="51" media="photo" title="Doc 51" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/51/51.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/51/in/album/5555" user_id="123"/>\n  <doc index="-2" doc_id="50" media="photo" title="Doc 50" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/50/50.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/50/in/album/5555" user_id="123"/>\n  (...)\n  <doc index="-18" doc_id="33" media="photo" title="Doc 68" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/33/33.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/33/in/album/5555" user_id="123"/>\n</prev>\n<doc index="0" doc_id="50" media="photo" title="Doc 50" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/50/50.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/50/in/album/5555" user_id="123"/>\n<next count="10">\n  <doc index="1" doc_id="52" media="photo" title="Doc 52" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/52/52.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/52/in/album/5555" user_id="123"/>\n  <doc index="2" doc_id="53" media="photo" title="Doc 53" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/53/53.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/53/in/album/5555" user_id="123"/>\n  (...)\n  <doc index="10" doc_id="61" media="photo" title="Doc 61" safety="1"\n       media="photo" w="75" h="75" url="http://u1.ipernity.com/1/00/61/61.d5ea56eb.75x.jpg" \n       link="http://www.ipernity.com/doc/123/61/in/album/5555" user_id="123"/>\n</next>', u'permissions': []
        }
        
    }
    