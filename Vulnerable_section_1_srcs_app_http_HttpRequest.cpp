 		path_ = request_target_.substr(0, query_delimiter);
 	}
 	decoded_path_ = DecodeUrl(path_);
	if (!IsValidPath_(path_)) {
 		state_ = RequestState::kInvalid;
 		return;
 	}
 	return !path.empty() && path[0] == '/';
 }
 
 void	HttpRequest::ParseHttpVersion_(const std::string &raw_request) {
 	if (!http_version_.empty()) {
 		return;