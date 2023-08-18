package com.example.hana.dto;

import com.example.hana.entity.User;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
public class UserDto {
//    @Size(min = 4 , max = 20 , message = "아이디는 4자 이상 , 20자 이하여야 합니다.")        // -> 프런트에서 처리
//    @NotBlank(message="아이디를 입력해주세요")
    private String userid;
    private String userpw;
    private String username;

    // 회원가입 객체
    public User toEntity() {
        return User.builder()
                .userid(userid)
                .userpw(userpw)
                .username(username)
                .usertime(LocalDateTime.now())
                .build();
    }
}
