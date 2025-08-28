   SetHost(nullptr, ec);
   UASSERT(!ec);
   if (!ec) {
    ec = std::error_code{static_cast<errc::UrlErrorCode>(native::curl_url_set(
        url_.get(), native::CURLUPART_URL, url, CURLU_DEFAULT_SCHEME))};
   }
 }
 