package com.example.hana.controller;

import com.example.hana.dto.resdto.AllResDto;
import com.example.hana.dto.UserDto;
import com.example.hana.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController     // json 으로 데이터를 주고받음을 선언
@RequestMapping("/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    // 개인 로그인
    @PostMapping("/login")
    public ResponseEntity<AllResDto> findUser(@RequestBody UserDto params) { //
        return null;
    }
}

