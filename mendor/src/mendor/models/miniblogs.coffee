

class miniBlog
	constructor: () ->
		@miniblog_schema = new Schema({
			mid: {type:String},
			uid: {},
			timestamp: {},
			imgs: [],
			medias: []
			})

		@flag_schema = new Schema({
			uid: {},
			maxmid: {}
			})

	find_blog_by_id: (id) ->
		return

	find_blogs_by_uid1: (uid,start,num) ->
		return

	find_blogs_by_uid2: (uid,mid, gt) ->
		return






module.exports = miniBlog