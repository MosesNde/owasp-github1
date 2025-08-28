 //
 //  httplib.h
 //
//  Copyright (c) 2024 Yuji Hirose. All rights reserved.
 //  MIT License
 //
 
 #ifndef CPPHTTPLIB_HTTPLIB_H
 #define CPPHTTPLIB_HTTPLIB_H
 
#define CPPHTTPLIB_VERSION "0.18.0"
 
 /*
  * Configuration
 #define CPPHTTPLIB_CLIENT_WRITE_TIMEOUT_USECOND 0
 #endif
 
 #ifndef CPPHTTPLIB_IDLE_INTERVAL_SECOND
 #define CPPHTTPLIB_IDLE_INTERVAL_SECOND 0
 #endif
 #endif
 
 using socket_t = SOCKET;
#ifdef CPPHTTPLIB_USE_POLL
 #define poll(fds, nfds, timeout) WSAPoll(fds, nfds, timeout)
#endif
 
 #else // not _WIN32
 
 #ifdef __linux__
 #include <resolv.h>
 #endif
 #include <netinet/tcp.h>
#ifdef CPPHTTPLIB_USE_POLL
 #include <poll.h>
#endif
#include <csignal>
 #include <pthread.h>
 #include <sys/mman.h>
#include <sys/select.h>
 #include <sys/socket.h>
 #include <sys/un.h>
 #include <unistd.h>
 
 inline bool equal(const std::string &a, const std::string &b) {
   return a.size() == b.size() &&
         std::equal(a.begin(), a.end(), b.begin(),
                    [](char ca, char cb) { return to_lower(ca) == to_lower(cb); });
 }
 
 struct equal_to {
 
 } // namespace detail
 
 enum StatusCode {
   // Information responses
   Continue_100 = 100,
 struct Request {
   std::string method;
   std::string path;
   Headers headers;
   std::string body;
 
   // for server
   std::string version;
   std::string target;
  Params params;
   MultipartFormDataMap files;
   Ranges ranges;
   Match matches;
   std::unordered_map<std::string, std::string> path_params;
 
   // for client
   ResponseHandler response_handler;
   ContentProvider content_provider_;
   bool is_chunked_content_provider_ = false;
   size_t authorization_count_ = 0;
 };
 
 struct Response {
   virtual ~Stream() = default;
 
   virtual bool is_readable() const = 0;
  virtual bool is_writable() const = 0;
 
   virtual ssize_t read(char *ptr, size_t size) = 0;
   virtual ssize_t write(const char *ptr, size_t size) = 0;
   virtual void get_remote_ip_and_port(std::string &ip, int &port) const = 0;
   virtual void get_local_ip_and_port(std::string &ip, int &port) const = 0;
   virtual socket_t socket() const = 0;
 
   ssize_t write(const char *ptr);
   ssize_t write(const std::string &s);
 };
 
 using SocketOptions = std::function<void(socket_t sock)>;
 
 void default_socket_options(socket_t sock);
 
 const char *status_message(int status);
  * Captures parameters in request path and stores them in Request::path_params
  *
  * Capture name is a substring of a pattern from : to /.
 * The rest of the pattern is matched agains the request path directly
  * Parameters are captured starting from the next character after
  * the end of the last matched static pattern fragment until the next /.
  *
   virtual bool process_and_close_socket(socket_t sock);
 
   std::atomic<bool> is_running_{false};
  std::atomic<bool> is_decommisioned{false};
 
   struct MountPointEntry {
     std::string mount_point;
   template <class Rep, class Period>
   void set_write_timeout(const std::chrono::duration<Rep, Period> &duration);
 
   void set_basic_auth(const std::string &username, const std::string &password);
   void set_bearer_token_auth(const std::string &token);
 #ifdef CPPHTTPLIB_OPENSSL_SUPPORT
 #ifdef CPPHTTPLIB_OPENSSL_SUPPORT
   void enable_server_certificate_verification(bool enabled);
   void enable_server_hostname_verification(bool enabled);
  void set_server_certificate_verifier(std::function<bool(SSL *ssl)> verifier);
 #endif
 
   void set_logger(Logger logger);
   time_t read_timeout_usec_ = CPPHTTPLIB_CLIENT_READ_TIMEOUT_USECOND;
   time_t write_timeout_sec_ = CPPHTTPLIB_CLIENT_WRITE_TIMEOUT_SECOND;
   time_t write_timeout_usec_ = CPPHTTPLIB_CLIENT_WRITE_TIMEOUT_USECOND;
 
   std::string basic_auth_username_;
   std::string basic_auth_password_;
 #ifdef CPPHTTPLIB_OPENSSL_SUPPORT
   bool server_certificate_verification_ = true;
   bool server_hostname_verification_ = true;
  std::function<bool(SSL *ssl)> server_certificate_verifier_;
 #endif
 
   Logger logger_;
 
   std::string adjust_host_string(const std::string &host) const;
 
  virtual bool process_socket(const Socket &socket,
                              std::function<bool(Stream &strm)> callback);
   virtual bool is_ssl() const;
 };
 
   template <class Rep, class Period>
   void set_write_timeout(const std::chrono::duration<Rep, Period> &duration);
 
   void set_basic_auth(const std::string &username, const std::string &password);
   void set_bearer_token_auth(const std::string &token);
 #ifdef CPPHTTPLIB_OPENSSL_SUPPORT
 #ifdef CPPHTTPLIB_OPENSSL_SUPPORT
   void enable_server_certificate_verification(bool enabled);
   void enable_server_hostname_verification(bool enabled);
  void set_server_certificate_verifier(std::function<bool(SSL *ssl)> verifier);
 #endif
 
   void set_logger(Logger logger);
   void shutdown_ssl(Socket &socket, bool shutdown_gracefully) override;
   void shutdown_ssl_impl(Socket &socket, bool shutdown_gracefully);
 
  bool process_socket(const Socket &socket,
                      std::function<bool(Stream &strm)> callback) override;
   bool is_ssl() const override;
 
  bool connect_with_proxy(Socket &sock, Response &res, bool &success,
                          Error &error);
   bool initialize_ssl(Socket &socket, Error &error);
 
   bool load_certs();
   callback(static_cast<time_t>(sec), static_cast<time_t>(usec));
 }
 
 inline uint64_t get_header_value_u64(const Headers &headers,
                                      const std::string &key, uint64_t def,
                                     size_t id) {
   auto rng = headers.equal_range(key);
   auto it = rng.first;
   std::advance(it, static_cast<ssize_t>(id));
   if (it != rng.second) {
    return std::strtoull(it->second.data(), nullptr, 10);
   }
   return def;
 }
 
 } // namespace detail
 
 inline uint64_t Request::get_header_value_u64(const std::string &key,
   return detail::get_header_value_u64(headers, key, def, id);
 }
 
inline void default_socket_options(socket_t sock) {
  int opt = 1;
 #ifdef _WIN32
  setsockopt(sock, SOL_SOCKET, SO_REUSEADDR,
             reinterpret_cast<const char *>(&opt), sizeof(opt));
  setsockopt(sock, SOL_SOCKET, SO_EXCLUSIVEADDRUSE,
             reinterpret_cast<const char *>(&opt), sizeof(opt));
 #else
#ifdef SO_REUSEPORT
  setsockopt(sock, SOL_SOCKET, SO_REUSEPORT,
             reinterpret_cast<const void *>(&opt), sizeof(opt));
 #else
  setsockopt(sock, SOL_SOCKET, SO_REUSEADDR,
             reinterpret_cast<const void *>(&opt), sizeof(opt));
 #endif
 #endif
 }
 
 inline const char *status_message(int status) {
       duration, [&](time_t sec, time_t usec) { set_write_timeout(sec, usec); });
 }
 
 template <class Rep, class Period>
 inline void Client::set_connection_timeout(
     const std::chrono::duration<Rep, Period> &duration) {
   cli_->set_write_timeout(duration);
 }
 
 /*
  * Forward declarations and types that will be part of the .h file if split into
  * .h + .cc.
 
 namespace detail {
 
 struct FileStat {
   FileStat(const std::string &path);
   bool is_file() const;
   bool is_dir() const;
 
 private:
   struct stat st_;
   int ret_ = -1;
 };
 
 void split(const char *b, const char *e, char d, size_t m,
            std::function<void(const char *, const char *)> fn);
 
bool process_client_socket(socket_t sock, time_t read_timeout_sec,
                           time_t read_timeout_usec, time_t write_timeout_sec,
                           time_t write_timeout_usec,
                           std::function<bool(Stream &)> callback);
 
 socket_t create_client_socket(const std::string &host, const std::string &ip,
                               int port, int address_family, bool tcp_nodelay,
   ~BufferStream() override = default;
 
   bool is_readable() const override;
  bool is_writable() const override;
   ssize_t read(char *ptr, size_t size) override;
   ssize_t write(const char *ptr, size_t size) override;
   void get_remote_ip_and_port(std::string &ip, int &port) const override;
   void get_local_ip_and_port(std::string &ip, int &port) const override;
   socket_t socket() const override;
 
   const std::string &get_buffer() const;
 
   char *fixed_buffer_;
   const size_t fixed_buffer_size_;
   size_t fixed_buffer_used_size_ = 0;
  std::string glowable_buffer_;
 };
 
 class mmap {
   bool is_open_empty_file = false;
 };
 
 } // namespace detail
 
 // ----------------------------------------------------------------------------
 }
 
 inline FileStat::FileStat(const std::string &path) {
   ret_ = stat(path.c_str(), &st_);
 }
 inline bool FileStat::is_file() const {
   return ret_ >= 0 && S_ISREG(st_.st_mode);
       fixed_buffer_size_(fixed_buffer_size) {}
 
 inline const char *stream_line_reader::ptr() const {
  if (glowable_buffer_.empty()) {
     return fixed_buffer_;
   } else {
    return glowable_buffer_.data();
   }
 }
 
 inline size_t stream_line_reader::size() const {
  if (glowable_buffer_.empty()) {
     return fixed_buffer_used_size_;
   } else {
    return glowable_buffer_.size();
   }
 }
 
 
 inline bool stream_line_reader::getline() {
   fixed_buffer_used_size_ = 0;
  glowable_buffer_.clear();
 
 #ifndef CPPHTTPLIB_ALLOW_LF_AS_LINE_TERMINATOR
   char prev_byte = 0;
     fixed_buffer_[fixed_buffer_used_size_++] = c;
     fixed_buffer_[fixed_buffer_used_size_] = '\0';
   } else {
    if (glowable_buffer_.empty()) {
       assert(fixed_buffer_[fixed_buffer_used_size_] == '\0');
      glowable_buffer_.assign(fixed_buffer_, fixed_buffer_used_size_);
     }
    glowable_buffer_ += c;
   }
 }
 
inline mmap::mmap(const char *path) {
  open(path);
}
 
 inline mmap::~mmap() { close(); }
 
 inline bool mmap::open(const char *path) {
   close();
 
 #if defined(_WIN32)
  std::wstring wpath;
  for (size_t i = 0; i < strlen(path); i++) {
    wpath += path[i];
  }
 
 #if _WIN32_WINNT >= _WIN32_WINNT_WIN8
   hFile_ = ::CreateFile2(wpath.c_str(), GENERIC_READ, FILE_SHARE_READ,
   });
 }
 
inline ssize_t select_read(socket_t sock, time_t sec, time_t usec) {
#ifdef CPPHTTPLIB_USE_POLL
  struct pollfd pfd_read;
  pfd_read.fd = sock;
  pfd_read.events = POLLIN;
 
   auto timeout = static_cast<int>(sec * 1000 + usec / 1000);
 
  return handle_EINTR([&]() { return poll(&pfd_read, 1, timeout); });
#else
#ifndef _WIN32
  if (sock >= FD_SETSIZE) { return -1; }
#endif

  fd_set fds;
  FD_ZERO(&fds);
  FD_SET(sock, &fds);

  timeval tv;
  tv.tv_sec = static_cast<long>(sec);
  tv.tv_usec = static_cast<decltype(tv.tv_usec)>(usec);
 
  return handle_EINTR([&]() {
    return select(static_cast<int>(sock + 1), &fds, nullptr, nullptr, &tv);
  });
#endif
 }
 
 inline ssize_t select_write(socket_t sock, time_t sec, time_t usec) {
#ifdef CPPHTTPLIB_USE_POLL
  struct pollfd pfd_read;
  pfd_read.fd = sock;
  pfd_read.events = POLLOUT;

  auto timeout = static_cast<int>(sec * 1000 + usec / 1000);

  return handle_EINTR([&]() { return poll(&pfd_read, 1, timeout); });
#else
#ifndef _WIN32
  if (sock >= FD_SETSIZE) { return -1; }
#endif

  fd_set fds;
  FD_ZERO(&fds);
  FD_SET(sock, &fds);

  timeval tv;
  tv.tv_sec = static_cast<long>(sec);
  tv.tv_usec = static_cast<decltype(tv.tv_usec)>(usec);

  return handle_EINTR([&]() {
    return select(static_cast<int>(sock + 1), nullptr, &fds, nullptr, &tv);
  });
#endif
 }
 
 inline Error wait_until_socket_is_ready(socket_t sock, time_t sec,
                                         time_t usec) {
#ifdef CPPHTTPLIB_USE_POLL
   struct pollfd pfd_read;
   pfd_read.fd = sock;
   pfd_read.events = POLLIN | POLLOUT;
   }
 
   return Error::Connection;
#else
#ifndef _WIN32
  if (sock >= FD_SETSIZE) { return Error::Connection; }
#endif

  fd_set fdsr;
  FD_ZERO(&fdsr);
  FD_SET(sock, &fdsr);

  auto fdsw = fdsr;
  auto fdse = fdsr;

  timeval tv;
  tv.tv_sec = static_cast<long>(sec);
  tv.tv_usec = static_cast<decltype(tv.tv_usec)>(usec);

  auto ret = handle_EINTR([&]() {
    return select(static_cast<int>(sock + 1), &fdsr, &fdsw, &fdse, &tv);
  });

  if (ret == 0) { return Error::ConnectionTimeout; }

  if (ret > 0 && (FD_ISSET(sock, &fdsr) || FD_ISSET(sock, &fdsw))) {
    auto error = 0;
    socklen_t len = sizeof(error);
    auto res = getsockopt(sock, SOL_SOCKET, SO_ERROR,
                          reinterpret_cast<char *>(&error), &len);
    auto successful = res >= 0 && !error;
    return successful ? Error::Success : Error::Connection;
  }
  return Error::Connection;
#endif
 }
 
 inline bool is_socket_alive(socket_t sock) {
 class SocketStream final : public Stream {
 public:
   SocketStream(socket_t sock, time_t read_timeout_sec, time_t read_timeout_usec,
               time_t write_timeout_sec, time_t write_timeout_usec);
   ~SocketStream() override;
 
   bool is_readable() const override;
  bool is_writable() const override;
   ssize_t read(char *ptr, size_t size) override;
   ssize_t write(const char *ptr, size_t size) override;
   void get_remote_ip_and_port(std::string &ip, int &port) const override;
   void get_local_ip_and_port(std::string &ip, int &port) const override;
   socket_t socket() const override;
 
 private:
   socket_t sock_;
   time_t read_timeout_sec_;
   time_t read_timeout_usec_;
   time_t write_timeout_sec_;
   time_t write_timeout_usec_;
 
   std::vector<char> read_buff_;
   size_t read_buff_off_ = 0;
 #ifdef CPPHTTPLIB_OPENSSL_SUPPORT
 class SSLSocketStream final : public Stream {
 public:
  SSLSocketStream(socket_t sock, SSL *ssl, time_t read_timeout_sec,
                  time_t read_timeout_usec, time_t write_timeout_sec,
                  time_t write_timeout_usec);
   ~SSLSocketStream() override;
 
   bool is_readable() const override;
  bool is_writable() const override;
   ssize_t read(char *ptr, size_t size) override;
   ssize_t write(const char *ptr, size_t size) override;
   void get_remote_ip_and_port(std::string &ip, int &port) const override;
   void get_local_ip_and_port(std::string &ip, int &port) const override;
   socket_t socket() const override;
 
 private:
   socket_t sock_;
   time_t read_timeout_usec_;
   time_t write_timeout_sec_;
   time_t write_timeout_usec_;
 };
 #endif
 
     } else {
       return true; // Ready for read
     }

    std::this_thread::sleep_for(microseconds{interval_usec});
   }
 
   return false;
       });
 }
 
inline bool process_client_socket(socket_t sock, time_t read_timeout_sec,
                                  time_t read_timeout_usec,
                                  time_t write_timeout_sec,
                                  time_t write_timeout_usec,
                                  std::function<bool(Stream &)> callback) {
   SocketStream strm(sock, read_timeout_sec, read_timeout_usec,
                    write_timeout_sec, write_timeout_usec);
   return callback(strm);
 }
 
     }
 #endif
 
    if (tcp_nodelay) {
      auto opt = 1;
#ifdef _WIN32
      setsockopt(sock, IPPROTO_TCP, TCP_NODELAY,
                 reinterpret_cast<const char *>(&opt), sizeof(opt));
#else
      setsockopt(sock, IPPROTO_TCP, TCP_NODELAY,
                 reinterpret_cast<const void *>(&opt), sizeof(opt));
#endif
    }
 
     if (rp->ai_family == AF_INET6) {
      auto opt = ipv6_v6only ? 1 : 0;
#ifdef _WIN32
      setsockopt(sock, IPPROTO_IPV6, IPV6_V6ONLY,
                 reinterpret_cast<const char *>(&opt), sizeof(opt));
#else
      setsockopt(sock, IPPROTO_IPV6, IPV6_V6ONLY,
                 reinterpret_cast<const void *>(&opt), sizeof(opt));
#endif
     }
 
     if (socket_options) { socket_options(sock); }
         }
 
         set_nonblocking(sock2, false);

        {
#ifdef _WIN32
          auto timeout = static_cast<uint32_t>(read_timeout_sec * 1000 +
                                               read_timeout_usec / 1000);
          setsockopt(sock2, SOL_SOCKET, SO_RCVTIMEO,
                     reinterpret_cast<const char *>(&timeout), sizeof(timeout));
#else
          timeval tv;
          tv.tv_sec = static_cast<long>(read_timeout_sec);
          tv.tv_usec = static_cast<decltype(tv.tv_usec)>(read_timeout_usec);
          setsockopt(sock2, SOL_SOCKET, SO_RCVTIMEO,
                     reinterpret_cast<const void *>(&tv), sizeof(tv));
#endif
        }
        {

#ifdef _WIN32
          auto timeout = static_cast<uint32_t>(write_timeout_sec * 1000 +
                                               write_timeout_usec / 1000);
          setsockopt(sock2, SOL_SOCKET, SO_SNDTIMEO,
                     reinterpret_cast<const char *>(&timeout), sizeof(timeout));
#else
          timeval tv;
          tv.tv_sec = static_cast<long>(write_timeout_sec);
          tv.tv_usec = static_cast<decltype(tv.tv_usec)>(write_timeout_usec);
          setsockopt(sock2, SOL_SOCKET, SO_SNDTIMEO,
                     reinterpret_cast<const void *>(&tv), sizeof(tv));
#endif
        }
 
         error = Error::Success;
         return true;
     p++;
   }
 
  if (p < end) {
     auto key_len = key_end - beg;
     if (!key_len) { return false; }
 
     auto key = std::string(beg, key_end);
    auto val = case_ignore::equal(key, "Location")
                   ? std::string(p, end)
                   : decode_url(std::string(p, end), false);

    // NOTE: From RFC 9110:
    // Field values containing CR, LF, or NUL characters are
    // invalid and dangerous, due to the varying ways that
    // implementations might parse and interpret those
    // characters; a recipient of CR, LF, or NUL within a field
    // value MUST either reject the message or replace each of
    // those characters with SP before further processing or
    // forwarding of that message.
    static const std::string CR_LF_NUL("\r\n\0", 3);
    if (val.find_first_of(CR_LF_NUL) != std::string::npos) { return false; }

    fn(key, val);
     return true;
   }
 
     auto end = line_reader.ptr() + line_reader.size() - line_terminator_len;
 
     if (!parse_header(line_reader.ptr(), end,
                      [&](const std::string &key, std::string &val) {
                         headers.emplace(key, val);
                       })) {
       return false;
   uint64_t r = 0;
   for (;;) {
     auto n = strm.read(buf, CPPHTTPLIB_RECV_BUFSIZ);
    if (n <= 0) { return true; }
 
     if (!out(buf, static_cast<size_t>(n), r, 0)) { return false; }
     r += static_cast<uint64_t>(n);
 
   assert(chunk_len == 0);
 
  // NOTE: In RFC 9112, '7.1 Chunked Transfer Coding' mentiones "The chunked
   // transfer coding is complete when a chunk with a chunk-size of zero is
   // received, possibly followed by a trailer section, and finally terminated by
   // an empty line". https://www.rfc-editor.org/rfc/rfc9112.html#section-7.1
   // to be ok whether the final CRLF exists or not in the chunked data.
   // https://www.rfc-editor.org/rfc/rfc9112.html#section-7.1.3
   //
  // According to the reference code in RFC 9112, cpp-htpplib now allows
  // chuncked transfer coding data without the final CRLF.
   if (!line_reader.getline()) { return true; }
 
   while (strcmp(line_reader.ptr(), "\r\n") != 0) {
         } else if (!has_header(x.headers, "Content-Length")) {
           ret = read_content_without_length(strm, out);
         } else {
          auto len = get_header_value_u64(x.headers, "Content-Length", 0, 0);
          if (len > payload_max_length) {
             exceed_payload_max_length = true;
             skip_content_with_length(strm, len);
             ret = false;
 
   data_sink.write = [&](const char *d, size_t l) -> bool {
     if (ok) {
      if (strm.is_writable() && write_data(strm, d, l)) {
         offset += l;
       } else {
         ok = false;
     return ok;
   };
 
  data_sink.is_writable = [&]() -> bool { return strm.is_writable(); };
 
   while (offset < end_offset && !is_shutting_down()) {
    if (!strm.is_writable()) {
       error = Error::Write;
       return false;
     } else if (!content_provider(offset, end_offset - offset, data_sink)) {
   data_sink.write = [&](const char *d, size_t l) -> bool {
     if (ok) {
       offset += l;
      if (!strm.is_writable() || !write_data(strm, d, l)) { ok = false; }
     }
     return ok;
   };
 
  data_sink.is_writable = [&]() -> bool { return strm.is_writable(); };
 
   data_sink.done = [&](void) { data_available = false; };
 
   while (data_available && !is_shutting_down()) {
    if (!strm.is_writable()) {
       return false;
     } else if (!content_provider(offset, 0, data_sink)) {
       return false;
           // Emit chunked response header and footer for each chunk
           auto chunk =
               from_i_to_hex(payload.size()) + "\r\n" + payload + "\r\n";
          if (!strm.is_writable() ||
              !write_data(strm, chunk.data(), chunk.size())) {
            ok = false;
          }
         }
       } else {
         ok = false;
     return ok;
   };
 
  data_sink.is_writable = [&]() -> bool { return strm.is_writable(); };
 
   auto done_with_trailer = [&](const Headers *trailer) {
     if (!ok) { return; }
     if (!payload.empty()) {
       // Emit chunked response header and footer for each chunk
       auto chunk = from_i_to_hex(payload.size()) + "\r\n" + payload + "\r\n";
      if (!strm.is_writable() ||
          !write_data(strm, chunk.data(), chunk.size())) {
         ok = false;
         return;
       }
   };
 
   while (data_available && !is_shutting_down()) {
    if (!strm.is_writable()) {
       error = Error::Write;
       return false;
     } else if (!content_provider(offset, 0, data_sink)) {
 
               it = params.find("filename*");
               if (it != params.end()) {
                // Only allow UTF-8 enconnding...
                 static const std::regex re_rfc5987_encoding(
                     R"~(^UTF-8''(.+?)$)~", std::regex_constants::icase);
 
 
 inline bool range_error(Request &req, Response &res) {
   if (!req.ranges.empty() && 200 <= res.status && res.status < 300) {
    ssize_t contant_len = static_cast<ssize_t>(
         res.content_length_ ? res.content_length_ : res.body.size());
 
     ssize_t prev_first_pos = -1;
 
       if (first_pos == -1 && last_pos == -1) {
         first_pos = 0;
        last_pos = contant_len;
       }
 
       if (first_pos == -1) {
        first_pos = contant_len - last_pos;
        last_pos = contant_len - 1;
       }
 
      if (last_pos == -1) { last_pos = contant_len - 1; }
 
       // Range must be within content length
       if (!(0 <= first_pos && first_pos <= last_pos &&
            last_pos <= contant_len - 1)) {
         return true;
       }
 
 
 inline bool expect_content(const Request &req) {
   if (req.method == "POST" || req.method == "PUT" || req.method == "PATCH" ||
      req.method == "PRI" || req.method == "DELETE") {
     return true;
   }
  // TODO: check if Content-Length is set
   return false;
 }
 
 inline std::string SHA_512(const std::string &s) {
   return message_digest(s, EVP_sha512());
 }
#endif
 
#ifdef CPPHTTPLIB_OPENSSL_SUPPORT
 #ifdef _WIN32
 // NOTE: This code came up with the following stackoverflow post:
 // https://stackoverflow.com/questions/9507184/can-openssl-on-windows-use-the-system-certificate-store
 static WSInit wsinit_;
 #endif
 
#ifdef CPPHTTPLIB_OPENSSL_SUPPORT
inline std::pair<std::string, std::string> make_digest_authentication_header(
    const Request &req, const std::map<std::string, std::string> &auth,
    size_t cnonce_count, const std::string &cnonce, const std::string &username,
    const std::string &password, bool is_proxy = false) {
  std::string nc;
  {
    std::stringstream ss;
    ss << std::setfill('0') << std::setw(8) << std::hex << cnonce_count;
    nc = ss.str();
  }

  std::string qop;
  if (auth.find("qop") != auth.end()) {
    qop = auth.at("qop");
    if (qop.find("auth-int") != std::string::npos) {
      qop = "auth-int";
    } else if (qop.find("auth") != std::string::npos) {
      qop = "auth";
    } else {
      qop.clear();
    }
  }

  std::string algo = "MD5";
  if (auth.find("algorithm") != auth.end()) { algo = auth.at("algorithm"); }

  std::string response;
  {
    auto H = algo == "SHA-256"   ? detail::SHA_256
             : algo == "SHA-512" ? detail::SHA_512
                                 : detail::MD5;

    auto A1 = username + ":" + auth.at("realm") + ":" + password;

    auto A2 = req.method + ":" + req.path;
    if (qop == "auth-int") { A2 += ":" + H(req.body); }

    if (qop.empty()) {
      response = H(H(A1) + ":" + auth.at("nonce") + ":" + H(A2));
    } else {
      response = H(H(A1) + ":" + auth.at("nonce") + ":" + nc + ":" + cnonce +
                   ":" + qop + ":" + H(A2));
    }
  }

  auto opaque = (auth.find("opaque") != auth.end()) ? auth.at("opaque") : "";

  auto field = "Digest username=\"" + username + "\", realm=\"" +
               auth.at("realm") + "\", nonce=\"" + auth.at("nonce") +
               "\", uri=\"" + req.path + "\", algorithm=" + algo +
               (qop.empty() ? ", response=\""
                            : ", qop=" + qop + ", nc=" + nc + ", cnonce=\"" +
                                  cnonce + "\", response=\"") +
               response + "\"" +
               (opaque.empty() ? "" : ", opaque=\"" + opaque + "\"");

  auto key = is_proxy ? "Proxy-Authorization" : "Authorization";
  return std::make_pair(key, field);
}
#endif

 inline bool parse_www_authenticate(const Response &res,
                                    std::map<std::string, std::string> &auth,
                                    bool is_proxy) {
 
 inline void Request::set_header(const std::string &key,
                                 const std::string &val) {
  if (!detail::has_crlf(key) && !detail::has_crlf(val)) {
     headers.emplace(key, val);
   }
 }
 
 inline void Response::set_header(const std::string &key,
                                  const std::string &val) {
  if (!detail::has_crlf(key) && !detail::has_crlf(val)) {
     headers.emplace(key, val);
   }
 }
 
 inline void Response::set_redirect(const std::string &url, int stat) {
  if (!detail::has_crlf(url)) {
     set_header("Location", url);
     if (300 <= stat && stat < 400) {
       this->status = stat;
 
 namespace detail {
 
 // Socket stream implementation
inline SocketStream::SocketStream(socket_t sock, time_t read_timeout_sec,
                                  time_t read_timeout_usec,
                                  time_t write_timeout_sec,
                                  time_t write_timeout_usec)
     : sock_(sock), read_timeout_sec_(read_timeout_sec),
       read_timeout_usec_(read_timeout_usec),
       write_timeout_sec_(write_timeout_sec),
      write_timeout_usec_(write_timeout_usec), read_buff_(read_buff_size_, 0) {}
 
 inline SocketStream::~SocketStream() = default;
 
 inline bool SocketStream::is_readable() const {
  return select_read(sock_, read_timeout_sec_, read_timeout_usec_) > 0;
 }
 
inline bool SocketStream::is_writable() const {
   return select_write(sock_, write_timeout_sec_, write_timeout_usec_) > 0 &&
          is_socket_alive(sock_);
 }
     }
   }
 
  if (!is_readable()) { return -1; }
 
   read_buff_off_ = 0;
   read_buff_content_size_ = 0;
 }
 
 inline ssize_t SocketStream::write(const char *ptr, size_t size) {
  if (!is_writable()) { return -1; }
 
 #if defined(_WIN32) && !defined(_WIN64)
   size =
 
 inline socket_t SocketStream::socket() const { return sock_; }
 
 // Buffer stream implementation
 inline bool BufferStream::is_readable() const { return true; }
 
inline bool BufferStream::is_writable() const { return true; }
 
 inline ssize_t BufferStream::read(char *ptr, size_t size) {
 #if defined(_MSC_VER) && _MSC_VER < 1910
 
 inline socket_t BufferStream::socket() const { return 0; }
 
 inline const std::string &BufferStream::get_buffer() const { return buffer; }
 
 inline PathParamsMatcher::PathParamsMatcher(const std::string &pattern) {
 inline bool Server::bind_to_port(const std::string &host, int port,
                                  int socket_flags) {
   auto ret = bind_internal(host, port, socket_flags);
  if (ret == -1) { is_decommisioned = true; }
   return ret >= 0;
 }
 inline int Server::bind_to_any_port(const std::string &host, int socket_flags) {
   auto ret = bind_internal(host, 0, socket_flags);
  if (ret == -1) { is_decommisioned = true; }
   return ret;
 }
 
 inline bool Server::is_running() const { return is_running_; }
 
 inline void Server::wait_until_ready() const {
  while (!is_running_ && !is_decommisioned) {
     std::this_thread::sleep_for(std::chrono::milliseconds{1});
   }
 }
     detail::shutdown_socket(sock);
     detail::close_socket(sock);
   }
  is_decommisioned = false;
 }
 
inline void Server::decommission() { is_decommisioned = true; }
 
 inline bool Server::parse_request_line(const char *s, Request &req) const {
   auto len = strlen(s);
 
 inline int Server::bind_internal(const std::string &host, int port,
                                  int socket_flags) {
  if (is_decommisioned) { return -1; }
 
   if (!is_valid()) { return -1; }
 
 }
 
 inline bool Server::listen_internal() {
  if (is_decommisioned) { return false; }
 
   auto ret = true;
   is_running_ = true;
 #endif
 
 #if defined _WIN32
      // sockets conneced via WASAccept inherit flags NO_HANDLE_INHERIT,
       // OVERLAPPED
       socket_t sock = WSAAccept(svr_sock_, nullptr, nullptr, nullptr, 0);
 #elif defined SOCK_CLOEXEC
         break;
       }
 
      {
#ifdef _WIN32
        auto timeout = static_cast<uint32_t>(read_timeout_sec_ * 1000 +
                                             read_timeout_usec_ / 1000);
        setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO,
                   reinterpret_cast<const char *>(&timeout), sizeof(timeout));
#else
        timeval tv;
        tv.tv_sec = static_cast<long>(read_timeout_sec_);
        tv.tv_usec = static_cast<decltype(tv.tv_usec)>(read_timeout_usec_);
        setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO,
                   reinterpret_cast<const void *>(&tv), sizeof(tv));
#endif
      }
      {

#ifdef _WIN32
        auto timeout = static_cast<uint32_t>(write_timeout_sec_ * 1000 +
                                             write_timeout_usec_ / 1000);
        setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO,
                   reinterpret_cast<const char *>(&timeout), sizeof(timeout));
#else
        timeval tv;
        tv.tv_sec = static_cast<long>(write_timeout_sec_);
        tv.tv_usec = static_cast<decltype(tv.tv_usec)>(write_timeout_usec_);
        setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO,
                   reinterpret_cast<const void *>(&tv), sizeof(tv));
#endif
      }
 
       if (!task_queue->enqueue(
               [this, sock]() { process_and_close_socket(sock); })) {
     task_queue->shutdown();
   }
 
  is_decommisioned = !ret;
   return ret;
 }
 
   res.version = "HTTP/1.1";
   res.headers = default_headers_;
 
#ifdef _WIN32
  // TODO: Increase FD_SETSIZE statically (libzmq), dynamically (MySQL).
#else
#ifndef CPPHTTPLIB_USE_POLL
  // Socket file descriptor exceeded FD_SETSIZE...
  if (strm.socket() >= FD_SETSIZE) {
    Headers dummy;
    detail::read_headers(strm, dummy);
    res.status = StatusCode::InternalServerError_500;
     return write_response(strm, close_connection, req, res);
   }
#endif
#endif
 
   // Check if the request URI doesn't exceed the limit
  if (line_reader.size() > CPPHTTPLIB_REQUEST_URI_MAX_LENGTH) {
     Headers dummy;
     detail::read_headers(strm, dummy);
     res.status = StatusCode::UriTooLong_414;
     return write_response(strm, close_connection, req, res);
   }
 
  // Request line and headers
  if (!parse_request_line(line_reader.ptr(), req) ||
      !detail::read_headers(strm, req.headers)) {
    res.status = StatusCode::BadRequest_400;
    return write_response(strm, close_connection, req, res);
  }

   if (req.get_header_value("Connection") == "close") {
     connection_closed = true;
   }
     }
   }
 
   // Routing
   auto routed = false;
 #ifdef CPPHTTPLIB_NO_EXCEPTIONS
                                       : StatusCode::PartialContent_206;
     }
 
    if (detail::range_error(req, res)) {
      res.body.clear();
      res.content_length_ = 0;
      res.content_provider_ = nullptr;
      res.status = StatusCode::RangeNotSatisfiable_416;
      return write_response(strm, close_connection, req, res);
    }

     // Serve file content by using a content provider
     if (!res.file_content_path_.empty()) {
       const auto &path = res.file_content_path_;
           });
     }
 
     return write_response_with_content(strm, close_connection, req, res);
   } else {
     if (res.status == -1) { res.status = StatusCode::NotFound_404; }
       client_cert_path_(client_cert_path), client_key_path_(client_key_path) {}
 
 inline ClientImpl::~ClientImpl() {
   std::lock_guard<std::mutex> guard(socket_mutex_);
   shutdown_socket(socket_);
   close_socket(socket_);
   read_timeout_usec_ = rhs.read_timeout_usec_;
   write_timeout_sec_ = rhs.write_timeout_sec_;
   write_timeout_usec_ = rhs.write_timeout_usec_;
   basic_auth_username_ = rhs.basic_auth_username_;
   basic_auth_password_ = rhs.basic_auth_password_;
   bearer_token_auth_token_ = rhs.bearer_token_auth_token_;
     auto is_alive = false;
     if (socket_.is_open()) {
       is_alive = detail::is_socket_alive(socket_.sock);
       if (!is_alive) {
        // Attempt to avoid sigpipe by shutting down nongracefully if it seems
         // like the other side has already closed the connection Also, there
         // cannot be any requests in flight from other threads since we locked
         // request_mutex_, so safe to close everything immediately
         auto &scli = static_cast<SSLClient &>(*this);
         if (!proxy_host_.empty() && proxy_port_ != -1) {
           auto success = false;
          if (!scli.connect_with_proxy(socket_, res, success, error)) {
             return success;
           }
         }
     }
   });
 
  ret = process_socket(socket_, [&](Stream &strm) {
     return handle_request(strm, req, res, close_connection, error);
   });
 
 
   if (!req.has_header("Accept")) { req.set_header("Accept", "*/*"); }
 
 #ifndef CPPHTTPLIB_NO_DEFAULT_USER_AGENT
  if (!req.has_header("User-Agent")) {
    auto agent = std::string("cpp-httplib/") + CPPHTTPLIB_VERSION;
    req.set_header("User-Agent", agent);
  }
 #endif
 
   if (req.body.empty()) {
     if (req.content_provider_) {
   {
     detail::BufferStream bstrm;
 
    const auto &path = url_encode_ ? detail::encode_url(req.path) : req.path;
     detail::write_request_line(bstrm, req.method, path);
 
     header_writer_(bstrm, req.headers);
   req.headers = headers;
   req.path = path;
   req.progress = progress;
 
   auto error = Error::Success;
 
   if (is_ssl()) {
     auto is_proxy_enabled = !proxy_host_.empty() && proxy_port_ != -1;
     if (!is_proxy_enabled) {
      char buf[1];
      if (SSL_peek(socket_.ssl, buf, 1) == 0 &&
          SSL_get_error(socket_.ssl, 0) == SSL_ERROR_ZERO_RETURN) {
         error = Error::SSLPeerCouldBeClosed_;
         return false;
       }
   // Body
   if ((res.status != StatusCode::NoContent_204) && req.method != "HEAD" &&
       req.method != "CONNECT") {
    auto redirect = 300 < res.status && res.status < 400 && follow_location_;
 
     if (req.response_handler && !redirect) {
       if (!req.response_handler(res)) {
             : static_cast<ContentReceiverWithProgress>(
                   [&](const char *buf, size_t n, uint64_t /*off*/,
                       uint64_t /*len*/) {
                    if (res.body.size() + n > res.body.max_size()) {
                      return false;
                    }
                     res.body.append(buf, n);
                     return true;
                   });
 
     if (res.has_header("Content-Length")) {
       if (!req.content_receiver) {
        auto len = std::min<size_t>(res.get_header_value_u64("Content-Length"),
                                    res.body.max_size());
        if (len > 0) { res.body.reserve(len); }
       }
     }
 
    int dummy_status;
    if (!detail::read_content(strm, res, (std::numeric_limits<size_t>::max)(),
                              dummy_status, std::move(progress), std::move(out),
                              decompress_)) {
      if (error != Error::Canceled) { error = Error::Read; }
      return false;
     }
   }
 
   };
 }
 
inline bool
ClientImpl::process_socket(const Socket &socket,
                           std::function<bool(Stream &strm)> callback) {
   return detail::process_client_socket(
       socket.sock, read_timeout_sec_, read_timeout_usec_, write_timeout_sec_,
      write_timeout_usec_, std::move(callback));
 }
 
 inline bool ClientImpl::is_ssl() const { return false; }
   req.path = path;
   req.headers = headers;
   req.progress = std::move(progress);
 
   return send_(std::move(req));
 }
         return content_receiver(data, data_length);
       };
   req.progress = std::move(progress);
 
   return send_(std::move(req));
 }
   req.method = "HEAD";
   req.headers = headers;
   req.path = path;
 
   return send_(std::move(req));
 }
   req.headers = headers;
   req.path = path;
   req.progress = progress;
 
   if (!content_type.empty()) { req.set_header("Content-Type", content_type); }
   req.body.assign(body, content_length);
   req.method = "OPTIONS";
   req.headers = headers;
   req.path = path;
 
   return send_(std::move(req));
 }
   write_timeout_usec_ = usec;
 }
 
 inline void ClientImpl::set_basic_auth(const std::string &username,
                                        const std::string &password) {
   basic_auth_username_ = username;
 }
 
 inline void ClientImpl::set_server_certificate_verifier(
    std::function<bool(SSL *ssl)> verifier) {
   server_certificate_verifier_ = verifier;
 }
 #endif
   // Note that it is not always possible to avoid SIGPIPE, this is merely a
   // best-efforts.
   if (shutdown_gracefully) {
#ifdef _WIN32
    SSL_shutdown(ssl);
#else
    timeval tv;
    tv.tv_sec = 1;
    tv.tv_usec = 0;
    setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO,
               reinterpret_cast<const void *>(&tv), sizeof(tv));

    auto ret = SSL_shutdown(ssl);
    while (ret == 0) {
      std::this_thread::sleep_for(std::chrono::milliseconds{100});
      ret = SSL_shutdown(ssl);
     }
#endif
   }
 
   std::lock_guard<std::mutex> guard(ctx_mutex);
 }
 
 template <typename T>
inline bool
process_client_socket_ssl(SSL *ssl, socket_t sock, time_t read_timeout_sec,
                          time_t read_timeout_usec, time_t write_timeout_sec,
                          time_t write_timeout_usec, T callback) {
   SSLSocketStream strm(sock, ssl, read_timeout_sec, read_timeout_usec,
                       write_timeout_sec, write_timeout_usec);
   return callback(strm);
 }
 
 };
 
 // SSL socket stream implementation
inline SSLSocketStream::SSLSocketStream(socket_t sock, SSL *ssl,
                                        time_t read_timeout_sec,
                                        time_t read_timeout_usec,
                                        time_t write_timeout_sec,
                                        time_t write_timeout_usec)
     : sock_(sock), ssl_(ssl), read_timeout_sec_(read_timeout_sec),
       read_timeout_usec_(read_timeout_usec),
       write_timeout_sec_(write_timeout_sec),
      write_timeout_usec_(write_timeout_usec) {
   SSL_clear_mode(ssl, SSL_MODE_AUTO_RETRY);
 }
 
 inline SSLSocketStream::~SSLSocketStream() = default;
 
 inline bool SSLSocketStream::is_readable() const {
  return detail::select_read(sock_, read_timeout_sec_, read_timeout_usec_) > 0;
 }
 
inline bool SSLSocketStream::is_writable() const {
   return select_write(sock_, write_timeout_sec_, write_timeout_usec_) > 0 &&
         is_socket_alive(sock_);
 }
 
 inline ssize_t SSLSocketStream::read(char *ptr, size_t size) {
   if (SSL_pending(ssl_) > 0) {
     return SSL_read(ssl_, ptr, static_cast<int>(size));
  } else if (is_readable()) {
     auto ret = SSL_read(ssl_, ptr, static_cast<int>(size));
     if (ret < 0) {
       auto err = SSL_get_error(ssl_, ret);
 #endif
         if (SSL_pending(ssl_) > 0) {
           return SSL_read(ssl_, ptr, static_cast<int>(size));
        } else if (is_readable()) {
           std::this_thread::sleep_for(std::chrono::microseconds{10});
           ret = SSL_read(ssl_, ptr, static_cast<int>(size));
           if (ret >= 0) { return ret; }
       }
     }
     return ret;
   }
  return -1;
 }
 
 inline ssize_t SSLSocketStream::write(const char *ptr, size_t size) {
  if (is_writable()) {
     auto handle_size = static_cast<int>(
         std::min<size_t>(size, (std::numeric_limits<int>::max)()));
 
 #else
       while (--n >= 0 && err == SSL_ERROR_WANT_WRITE) {
 #endif
        if (is_writable()) {
           std::this_thread::sleep_for(std::chrono::microseconds{10});
           ret = SSL_write(ssl_, ptr, static_cast<int>(handle_size));
           if (ret >= 0) { return ret; }
 
 inline socket_t SSLSocketStream::socket() const { return sock_; }
 
 static SSLInit sslinit_;
 
 } // namespace detail
 }
 
 // Assumes that socket_mutex_ is locked and that there are no requests in flight
inline bool SSLClient::connect_with_proxy(Socket &socket, Response &res,
                                          bool &success, Error &error) {
   success = true;
   Response proxy_res;
   if (!detail::process_client_socket(
           socket.sock, read_timeout_sec_, read_timeout_usec_,
          write_timeout_sec_, write_timeout_usec_, [&](Stream &strm) {
             Request req2;
             req2.method = "CONNECT";
             req2.path = host_and_port_;
             return process_request(strm, req2, proxy_res, false, error);
           })) {
     // Thread-safe to close everything because we are assuming there are no
         proxy_res = Response();
         if (!detail::process_client_socket(
                 socket.sock, read_timeout_sec_, read_timeout_usec_,
                write_timeout_sec_, write_timeout_usec_, [&](Stream &strm) {
                   Request req3;
                   req3.method = "CONNECT";
                   req3.path = host_and_port_;
                   req3.headers.insert(detail::make_digest_authentication_header(
                       req3, auth, 1, detail::random_string(10),
                       proxy_digest_auth_username_, proxy_digest_auth_password_,
                       true));
                   return process_request(strm, req3, proxy_res, false, error);
                 })) {
           // Thread-safe to close everything because we are assuming there are
         }
 
         if (server_certificate_verification_) {
           if (server_certificate_verifier_) {
            if (!server_certificate_verifier_(ssl2)) {
              error = Error::SSLServerVerification;
              return false;
            }
          } else {
             verify_result_ = SSL_get_verify_result(ssl2);
 
             if (verify_result_ != X509_V_OK) {
   assert(socket.ssl == nullptr);
 }
 
inline bool
SSLClient::process_socket(const Socket &socket,
                          std::function<bool(Stream &strm)> callback) {
   assert(socket.ssl);
   return detail::process_client_socket_ssl(
       socket.ssl, socket.sock, read_timeout_sec_, read_timeout_usec_,
      write_timeout_sec_, write_timeout_usec_, std::move(callback));
 }
 
 inline bool SSLClient::is_ssl() const { return true; }
 
   auto type = GEN_DNS;
 
  struct in6_addr addr6 {};
  struct in_addr addr {};
   size_t addr_len = 0;
 
 #ifndef __MINGW32__
 }
 
 inline void Client::set_server_certificate_verifier(
    std::function<bool(SSL *ssl)> verifier) {
   cli_->set_server_certificate_verifier(verifier);
 }
 #endif
 
 } // namespace httplib
 
#if defined(_WIN32) && defined(CPPHTTPLIB_USE_POLL)
 #undef poll
 #endif
 