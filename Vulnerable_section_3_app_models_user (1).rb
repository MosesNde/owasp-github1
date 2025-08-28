 # frozen_string_literal: true
 # == Schema Information
 #
 # Table name: users
 #  third_party_avatar     :text
 #  failed_attempts        :integer          default(0), not null
 #  locked_at              :datetime
 #
# rubocop:disable Metrics/ClassLength
 class User < ApplicationRecord
   include AllyConcern
 
     in: Rails.application.config.i18n.available_locales.map(&:to_s).push(nil)
   }
 
   def active_for_authentication?
     super && !banned
   end
     super
   end
 end
# rubocop:enable Metrics/ClassLength