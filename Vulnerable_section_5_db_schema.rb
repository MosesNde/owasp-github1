 #
 # It's strongly recommended that you check this file into your version control system.
 
ActiveRecord::Schema.define(version: 2021_10_05_010735) do
 
   # These are extensions that must be enabled in order to support this database
   enable_extension "plpgsql"
     t.datetime "confirmed_at"
     t.datetime "confirmation_sent_at"
     t.string "unconfirmed_email"
     t.index ["confirmation_token"], name: "index_users_on_confirmation_token", unique: true
     t.index ["email"], name: "index_users_on_email", unique: true
     t.index ["invitation_token"], name: "index_users_on_invitation_token", unique: true